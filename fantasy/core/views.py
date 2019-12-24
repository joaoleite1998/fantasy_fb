from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

from core.models import Roster, Player, Letter, Position, Team
from core.data import *
from core.web_scraper import *
from core.data_processor import *

import requests
from datetime import datetime

"""
Views
"""
# splash view
def splash(request):
    return render(request, "splash.html", {})


# view for when user enters credentials
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return home_view(request)

    fantasy_users = User.objects.all

    return render(request, 'accounts.html', {})

def logout_view(request):
    logout(request)
    return redirect("/login")

# view called when signs up
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # creates user account and new roster with user id
        user = User.objects.create_user(username=username, email=email, password=password)    
        roster = Roster.objects.create(owner_id=user.id, created_at=datetime.now()) 
        roster.save()

    return redirect('/')

# home page after logging in, shows user's roster
def home_view(request):
    user_id = request.user.id
    roster = Roster.objects.get(owner_id=user_id)
    info = get_roster_info(roster)
    return render(request, 'home.html', info)


# navigates to players to draft, based on position and availability
def search_player_to_draft_view(request):
    player_key = request.GET['player_key']
    if player_key == "FLEX":
        players = Player.objects.all()
    else:
        pos_key = player_pos_keys[player_key]
        position = Position.objects.get(pos_key=pos_key)
        players = position.players.all

    if players:
        return render(request, 'draft_players.html', {"player_key": player_key, "players": players})
    else:
        return render(request, 'draft_players.html', {"player_key": player_key, "players": []})

# returns to home after user drafts a player
def draft_player_view(request):
    user_id = request.user.id
    player_key = request.GET['player_key']
    player_id = request.GET['player_id']

    roster = Roster.objects.get(owner_id=user_id)
    player = Player.objects.get(id=player_id)
    player.available = False
    player.save()

    update_roster_info(roster, player_key, player_id)
    info = get_roster_info(roster)
    return render(request, 'home.html', info)

# view called for when user drops a player
def drop_player_view(request):
    user_id = request.user.id
    player_key = request.GET['player_key']

    player_id = int(request.GET['player_id'])
    player = Player.objects.get(id=player_id)
    player.available = True
    player.save()

    roster = Roster.objects.get(owner_id=user_id)
    update_roster_info(roster, player_key, 0)
    info = get_roster_info(roster)
    return render(request, 'home.html', info)

# view that leads to page with all player search options (letter, position, team or all players)
def find_players_view(request):
    players_sort_keys = {"letter_chars": letter_chars, "pos_leg": pos_abbr.items(), "team_leg": team_abbr.items()}
    return render(request, 'find_players.html', players_sort_keys)

# view that shows player's fantasy performance in previous seasons
def player_stats_view(request):
    player_id = request.GET['player_id']
    player = Player.objects.get(id=player_id)

    prev_fantasy_pts = find_previous_years_stats(player.stats_url)
    num_seasons = len(prev_fantasy_pts)
    avg_pts = np.mean([pts for yr, pts in prev_fantasy_pts.items()])
    return render(request, 'previous_stats.html', {"player": player, "num_seasons": num_seasons, "avg_pts": avg_pts, "prev_stats": prev_fantasy_pts.items()})

# view that shows all interesting players without any filter
def all_players_view(request):
    players = Player.objects.all()
    return render(request, 'players.html', {"players": players})

# view that shows all interesting players that have certain letter
def letter_view(request):
    letter_char = request.GET['letter_char']
    letter = Letter.objects.get(letter_char=letter_char)
    players = letter.players.all

    # might not have any players
    if players:
        return render(request, 'players.html', {"players": players})
    else:
        return render(request, 'players.html', {"players": []})

# view that shows all interesting players that play in a certain position
def position_view(request):
    pos_key = request.GET['pos_key']
    position = Position.objects.get(pos_key=pos_key)
    players = position.players.all
    if players:
        return render(request, 'players.html', {"players": players})
    else:
        return render(request, 'players.html', {"players": []})

# view that shows all interesting players that play in a certain team
def team_view(request):
    team_key = request.GET['team_key']
    team = Team.objects.get(team_key=team_key)
    players = team.players.all
    if players:
        return render(request, 'players.html', {"players": players})
    else:
        return render(request, 'players.html', {"players": []})

# calls method to update player statistics and returns to home
def update_stat_view(request):
    update_fantasy_pts()
    roster = Roster.objects.get(owner_id=request.user.id)
    info = get_roster_info(roster)
    return render(request, 'home.html', info)

"""
view that clears and repopulates all tables for players, positions, letters and teams. 
Triggered manually when clicking the populate all data button.
Takes around 2 minutes to execute
"""
def repopulate_all_tables_view(request):
    depopulate_all_tables()
    populate_all_tables()
    update_fantasy_pts()

    user_id = request.user.id
    roster = Roster.objects.get(owner_id=user_id)
    info = get_roster_info(roster)
    return render(request, 'home.html', info)
