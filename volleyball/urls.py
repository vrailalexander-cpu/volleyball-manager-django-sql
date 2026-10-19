from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('players/', views.PlayerListView.as_view(), name='player-list'),
    path('players/add/', views.PlayerCreateView.as_view(), name='player-create'),
    path('players/<int:pk>/', views.PlayerDetailView.as_view(), name='player-detail'),
    path('players/<int:pk>/edit/', views.PlayerUpdateView.as_view(), name='player-update'),
    path('players/<int:pk>/delete/', views.PlayerDeleteView.as_view(), name='player-delete'),
    path('trainings/', views.TrainingListView.as_view(), name='training-list'),
    path('trainings/add/', views.TrainingCreateView.as_view(), name='training-create'),
    path('trainings/<int:pk>/', views.TrainingDetailView.as_view(), name='training-detail'),
    path('trainings/<int:pk>/edit/', views.TrainingUpdateView.as_view(), name='training-update'),
    path('trainings/<int:pk>/delete/', views.TrainingDeleteView.as_view(), name='training-delete'),
    path('competitions/', views.CompetitionListView.as_view(), name='competition-list'),
    path('competitions/add/', views.CompetitionCreateView.as_view(), name='competition-create'),
    path('competitions/<int:pk>/', views.CompetitionDetailView.as_view(), name='competition-detail'),
    path('competitions/<int:pk>/edit/', views.CompetitionUpdateView.as_view(), name='competition-update'),
    path('competitions/<int:pk>/delete/', views.CompetitionDeleteView.as_view(), name='competition-delete'),
    path('matches/', views.MatchListView.as_view(), name='match-list'),
    path('matches/add/', views.MatchCreateView.as_view(), name='match-create'),
    path('matches/<int:pk>/', views.MatchDetailView.as_view(), name='match-detail'),
    path('matches/<int:pk>/edit/', views.MatchUpdateView.as_view(), name='match-update'),
    path('matches/<int:pk>/delete/', views.MatchDeleteView.as_view(), name='match-delete'),
    path('attendance/', views.AttendanceListView.as_view(), name='attendance-list'),
    path('attendance/add/', views.AttendanceCreateView.as_view(), name='attendance-create'),
]