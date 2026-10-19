from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Player, Training, Competition, Match, Attendance, Team, Coach
from .forms import PlayerForm, TrainingForm, CompetitionForm, MatchForm, AttendanceForm

class HomeView(TemplateView):
    template_name = 'volleyball/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'players_count': Player.objects.count(),
            'trainings_count': Training.objects.count(),
            'competitions_count': Competition.objects.count(),
            'matches_count': Match.objects.count(),
            'upcoming_trainings': Training.objects.select_related('team').order_by('starts_at')[:5],
        })
        return context

class PlayerListView(ListView):
    model = Player
    template_name = 'volleyball/player_list.html'
    context_object_name = 'players'
    paginate_by = 10

class PlayerDetailView(DetailView):
    model = Player
    template_name = 'volleyball/player_detail.html'
    context_object_name = 'player'

class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerForm
    template_name = 'volleyball/form.html'
    success_url = reverse_lazy('player-list')
    extra_context = {'page_title': 'Додати гравця'}

class PlayerUpdateView(UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = 'volleyball/form.html'
    success_url = reverse_lazy('player-list')
    extra_context = {'page_title': 'Редагувати гравця'}

class PlayerDeleteView(DeleteView):
    model = Player
    template_name = 'volleyball/confirm_delete.html'
    success_url = reverse_lazy('player-list')
    extra_context = {'page_title': 'Видалити гравця'}

class TrainingListView(ListView):
    model = Training
    template_name = 'volleyball/training_list.html'
    context_object_name = 'trainings'
    paginate_by = 10

class TrainingDetailView(DetailView):
    model = Training
    template_name = 'volleyball/training_detail.html'
    context_object_name = 'training'

class TrainingCreateView(CreateView):
    model = Training
    form_class = TrainingForm
    template_name = 'volleyball/form.html'
    success_url = reverse_lazy('training-list')
    extra_context = {'page_title': 'Запланувати тренування'}

class TrainingUpdateView(UpdateView):
    model = Training
    form_class = TrainingForm
    template_name = 'volleyball/form.html'
    success_url = reverse_lazy('training-list')
    extra_context = {'page_title': 'Редагувати тренування'}

class TrainingDeleteView(DeleteView):
    model = Training
    template_name = 'volleyball/confirm_delete.html'
    success_url = reverse_lazy('training-list')
    extra_context = {'page_title': 'Видалити тренування'}

class CompetitionListView(ListView):
    model = Competition
    template_name = 'volleyball/competition_list.html'
    context_object_name = 'competitions'

class CompetitionDetailView(DetailView):
    model = Competition
    template_name = 'volleyball/competition_detail.html'
    context_object_name = 'competition'

class CompetitionCreateView(CreateView):
    model = Competition
    form_class = CompetitionForm
    template_name = 'volleyball/form.html'
    success_url = reverse_lazy('competition-list')
    extra_context = {'page_title': 'Додати змагання'}

class CompetitionUpdateView(UpdateView):
    model = Competition
    form_class = CompetitionForm
    template_name = 'volleyball/form.html'
    success_url = reverse_lazy('competition-list')
    extra_context = {'page_title': 'Редагувати змагання'}

class CompetitionDeleteView(DeleteView):
    model = Competition
    template_name = 'volleyball/confirm_delete.html'
    success_url = reverse_lazy('competition-list')
    extra_context = {'page_title': 'Видалити змагання'}

class MatchListView(ListView):
    model = Match
    template_name = 'volleyball/match_list.html'
    context_object_name = 'matches'

class MatchDetailView(DetailView):
    model = Match
    template_name = 'volleyball/match_detail.html'
    context_object_name = 'match'

class MatchCreateView(CreateView):
    model = Match
    form_class = MatchForm
    template_name = 'volleyball/form.html'
    success_url = reverse_lazy('match-list')
    extra_context = {'page_title': 'Додати матч'}

class MatchUpdateView(UpdateView):
    model = Match
    form_class = MatchForm
    template_name = 'volleyball/form.html'
    success_url = reverse_lazy('match-list')
    extra_context = {'page_title': 'Редагувати матч'}

class MatchDeleteView(DeleteView):
    model = Match
    template_name = 'volleyball/confirm_delete.html'
    success_url = reverse_lazy('match-list')
    extra_context = {'page_title': 'Видалити матч'}

class AttendanceListView(ListView):
    model = Attendance
    template_name = 'volleyball/attendance_list.html'
    context_object_name = 'records'

class AttendanceCreateView(CreateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = 'volleyball/form.html'
    success_url = reverse_lazy('attendance-list')
    extra_context = {'page_title': 'Додати відвідуваність'}
