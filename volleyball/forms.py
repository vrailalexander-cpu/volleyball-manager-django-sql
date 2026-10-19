from django import forms
from .models import Player, Training, Competition, Match, Attendance, Team, Coach

class StyledModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'form-control')

class PlayerForm(StyledModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'birth_date', 'position', 'jersey_number', 'team']
        widgets = {'birth_date': forms.DateInput(attrs={'type': 'date'})}

class TrainingForm(StyledModelForm):
    class Meta:
        model = Training
        fields = ['team', 'coach', 'starts_at', 'duration_minutes', 'location', 'notes']
        widgets = {'starts_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['starts_at'].input_formats = ['%Y-%m-%dT%H:%M']

class CompetitionForm(StyledModelForm):
    class Meta:
        model = Competition
        fields = ['name', 'location', 'start_date', 'end_date', 'competition_type']
        widgets = {'start_date': forms.DateInput(attrs={'type': 'date'}), 'end_date': forms.DateInput(attrs={'type': 'date'})}

    def clean(self):
        cleaned = super().clean()
        start, end = cleaned.get('start_date'), cleaned.get('end_date')
        if start and end and end < start:
            self.add_error('end_date', 'Дата завершення не може бути раніше дати початку.')
        return cleaned

class MatchForm(StyledModelForm):
    class Meta:
        model = Match
        fields = ['competition', 'home_team', 'away_team', 'starts_at', 'home_score', 'away_score', 'status']
        widgets = {'starts_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['starts_at'].input_formats = ['%Y-%m-%dT%H:%M']

    def clean(self):
        cleaned = super().clean()
        if cleaned.get('home_team') and cleaned.get('home_team') == cleaned.get('away_team'):
            self.add_error('away_team', 'Команди матчу мають бути різними.')
        return cleaned

class AttendanceForm(StyledModelForm):
    class Meta:
        model = Attendance
        fields = ['training', 'player', 'status', 'comment']