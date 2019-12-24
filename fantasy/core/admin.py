from django.contrib import admin
from django.contrib.auth.models import User
from core.models import Player, Letter, Position, Team, Roster

# Register your models here.
admin.site.register(Player)
admin.site.register(Letter)
admin.site.register(Position)
admin.site.register(Team)
admin.site.register(Roster)
