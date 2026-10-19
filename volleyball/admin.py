from django.contrib import admin
from .models import Coach, Player, Team, Training, Attendance, Competition, Match

admin.site.register(
    [Coach,
    Player,
    Team,
    Training,
    Attendance,
    Competition,
    Match
    ]
)