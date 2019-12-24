"""fantasy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', splash, name='splash'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('signup', signup_view, name='signup'),
    path('home', home_view, name='home'),
    path('players', all_players_view, name='players'),
    path('letter', letter_view, name='letter'),
    path('position', position_view, name='position'),
    path('team', team_view, name='team'),
    path('search_player_to_draft', search_player_to_draft_view, name='search_player_to_draft'),
    path('draft_player', draft_player_view, name='draft_player'),
    path('drop_player', drop_player_view, name='drop_player'),
    path('find_players', find_players_view, name='find_players'),
    path('player_stats', player_stats_view, name='player_stats'),
    path('update', update_stat_view, name='update'),
    path('populate_database', repopulate_all_tables_view, name='populate_database'),
]
