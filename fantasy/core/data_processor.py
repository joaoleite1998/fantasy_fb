from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

from core.models import Roster, Player, Letter, Position, Team
from core.data import *
from core.data_processor import *
from math import fsum

import requests

"""
Letter methods
"""


# delete all letters from dB
def depopulate_letters_table():
    letters = Letter.objects.all()
    for letter in letters:
        letter.delete()

# assign players to letters relationship
def populate_letters_table():
    letter_players = {chr(i): [] for i in range(ord('A'), ord('Z') + 1)}
    players = Player.objects.all()
    for player in players:
        letter_char = player.letter_char
        letter_players[letter_char].append(player)

    for letter_char in letter_players:
        letter = Letter.objects.create(letter_char=letter_char)
        for player in letter_players[letter_char]:
            letter.players.add(player)

        letter.save()


"""
Position methods
"""

# delete all positions from dB
def depopulate_positions_table():
    positions = Position.objects.all()
    for pos in positions:
        pos.delete()

# assign players to positions relationship
def populate_positions_table():
    players = Player.objects.all()
    pos_players_dict = {pos_key: [] for pos_key in pos_abbr}
    for player in players:
        pos_key = player.pos_key
        pos_players_dict[pos_key].append(player)

    for pos_key in pos_players_dict:
        pos = Position.objects.create(pos_key=pos_key)
        for player in pos_players_dict[pos_key]:
            pos.players.add(player)

        pos.save()

"""
Teams methods
"""

# delete all teams from dB
def depopulate_teams_table():
    teams = Team.objects.all()
    for team in teams:
        team.delete()

# assign teams to positions relationship
def populate_teams_table():
    players = Player.objects.all()
    team_players_dict = {team_name: [] for team_name in team_abbr}
    for player in players:
        player_team = player.team_name
        team_players_dict[player_team].append(player)


    for team_name in team_players_dict:
        team_key = team_abbr[team_name]
        team = Team.objects.create(team_key=team_key, team_name=team_name)
        for player in team_players_dict[team_name]:
            team.players.add(player)

        team.save()

"""
Roster info
"""
# assigns a roster position (QB, RB1 etc.) to a player's id
def update_roster_info(roster, player_key, player_id):

    if player_key == 'QB':
        roster.qb_id = player_id
    elif player_key == 'RB1':
        roster.rb_one_id = player_id
    elif player_key == 'RB2':
        roster.rb_two_id = player_id
    elif player_key == 'WR1':
        roster.wr_one_id = player_id
    elif player_key == 'WR2':
        roster.wr_two_id = player_id
    elif player_key == 'WR3':
        roster.wr_three_id = player_id
    elif player_key == 'TE':
        roster.te_id = player_id
    elif player_key == 'FLEX':
        roster.flex_id = player_id

    roster.save()

# fetches player with certain id, if player exists
def get_player(player_id):
    if Player.objects.filter(id=player_id):
        return Player.objects.get(id=player_id)
    else:
        return None

# sums all fantasy points in a user's roster
def calc_tot_points(roster):
    roster_pts = [get_player(p_id).fantasy_pts for p_id in roster if get_player(p_id)] 
    return fsum(roster_pts)

# gets all players in roster and returns as an object
def get_roster_info(roster):
    qb = get_player(roster.qb_id)
    rb_one = get_player(roster.rb_one_id)
    rb_two = get_player(roster.rb_two_id)
    wr_one = get_player(roster.wr_one_id)
    wr_two = get_player(roster.wr_two_id)
    wr_three = get_player(roster.wr_three_id)
    te = get_player(roster.te_id)
    flex = get_player(roster.flex_id)

    total_pts = calc_tot_points(roster)
    info = {"roster": roster, "qb": qb, "rb_one": rb_one, "rb_two": rb_two, "wr_one": wr_one, "wr_two": wr_two, "wr_three": wr_three, "te": te, "flex": flex, "total_pts": total_pts}
    return info


def get_users_total_points():
    users = User.objects.all()
    user_pts = {}
    for user in users:
        if user.username != 'joaoadmin':
            username = user.username
            roster = Roster.objects.get(owner_id=user.id)
            pts = calc_tot_points(roster)
            user_pts[username] = pts

    return user_pts.items()
        

