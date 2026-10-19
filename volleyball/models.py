from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Coach(models.Model):
    first_name = models.CharField('Ім’я', max_length=50)
    last_name = models.CharField('Прізвище', max_length=50)
    phone = models.CharField('Телефон', max_length=20, blank=True)
    email = models.EmailField('Електронна пошта', blank=True)

    class Meta:
        verbose_name = 'тренер'
        verbose_name_plural = 'Тренери'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Player(models.Model):
    POSITIONS = [
        ('setter', 'Зв’язуючий'), ('opposite', 'Діагональний'),
        ('outside', 'Догравальник'), ('middle', 'Центральний блокуючий'),
        ('libero', 'Ліберо'),
    ]
    first_name = models.CharField('Ім’я', max_length=50)
    last_name = models.CharField('Прізвище', max_length=50)
    birth_date = models.DateField('Дата народження', null=True, blank=True)
    position = models.CharField('Ігрова позиція', max_length=20, choices=POSITIONS)
    jersey_number = models.PositiveSmallIntegerField('Номер на формі', validators=[MinValueValidator(1), MaxValueValidator(99)])
    team = models.ForeignKey('Team', verbose_name='Команда', on_delete=models.SET_NULL, null=True, blank=True, related_name='players')

    class Meta:
        verbose_name = 'гравець'
        verbose_name_plural = 'Гравці'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name} (№{self.jersey_number})'

class Team(models.Model):
    name = models.CharField('Назва команди', max_length=100, unique=True)
    category = models.CharField('Категорія', max_length=50, blank=True)
    coach = models.ForeignKey(Coach, verbose_name='Тренер', on_delete=models.SET_NULL, null=True, blank=True, related_name='teams')

    class Meta:
        verbose_name = 'команда'
        verbose_name_plural = 'Команди'
        ordering = ['name']

    def __str__(self):
        return self.name

class Training(models.Model):
    team = models.ForeignKey(Team, verbose_name='Команда', on_delete=models.CASCADE, related_name='trainings')
    coach = models.ForeignKey(Coach, verbose_name='Тренер', on_delete=models.SET_NULL, null=True, blank=True, related_name='trainings')
    starts_at = models.DateTimeField('Дата та час')
    duration_minutes = models.PositiveSmallIntegerField('Тривалість (хвилини)', default=90, validators=[MinValueValidator(1)])
    location = models.CharField('Місце проведення', max_length=150)
    notes = models.TextField('Примітки', blank=True)

    class Meta:
        verbose_name = 'тренування'
        verbose_name_plural = 'Тренування'
        ordering = ['-starts_at']

    def __str__(self):
        return f'{self.team} — {self.starts_at:%d.%m.%Y %H:%M}'

class Attendance(models.Model):
    STATUSES = [('present', 'Присутній'), ('absent', 'Відсутній'), ('late', 'Запізнився'), ('excused', 'Поважна причина')]
    training = models.ForeignKey(Training, verbose_name='Тренування', on_delete=models.CASCADE, related_name='attendance')
    player = models.ForeignKey(Player, verbose_name='Гравець', on_delete=models.CASCADE, related_name='attendance')
    status = models.CharField('Статус', max_length=10, choices=STATUSES, default='present')
    comment = models.CharField('Коментар', max_length=255, blank=True)

    class Meta:
        verbose_name = 'відвідування'
        verbose_name_plural = 'Відвідуваність'
        constraints = [models.UniqueConstraint(fields=['training', 'player'], name='unique_player_training_attendance')]

    def __str__(self):
        return f'{self.player} — {self.get_status_display()}'

class Competition(models.Model):
    TYPES = [('cup', 'Кубок'), ('championship', 'Чемпіонат'), ('friendly', 'Товариський турнір')]
    name = models.CharField('Назва змагання', max_length=150)
    location = models.CharField('Місце проведення', max_length=150, blank=True)
    start_date = models.DateField('Дата початку')
    end_date = models.DateField('Дата завершення')
    competition_type = models.CharField('Тип змагання', max_length=20, choices=TYPES, default='championship')

    class Meta:
        verbose_name = 'змагання'
        verbose_name_plural = 'Змагання'
        ordering = ['-start_date']

    def __str__(self):
        return self.name

class Match(models.Model):
    STATUSES = [('planned', 'Запланований'), ('completed', 'Завершений'), ('cancelled', 'Скасований')]
    competition = models.ForeignKey(Competition, verbose_name='Змагання', on_delete=models.CASCADE, related_name='matches')
    home_team = models.ForeignKey(Team, verbose_name='Господарі', on_delete=models.PROTECT, related_name='home_matches')
    away_team = models.ForeignKey(Team, verbose_name='Гості', on_delete=models.PROTECT, related_name='away_matches')
    starts_at = models.DateTimeField('Дата та час матчу')
    home_score = models.PositiveSmallIntegerField('Очки господарів', default=0)
    away_score = models.PositiveSmallIntegerField('Очки гостей', default=0)
    status = models.CharField('Статус матчу', max_length=12, choices=STATUSES, default='planned')

    class Meta:
        verbose_name = 'матч'
        verbose_name_plural = 'Матчі'
        ordering = ['-starts_at']

    def __str__(self):
        return f'{self.home_team} — {self.away_team}'
