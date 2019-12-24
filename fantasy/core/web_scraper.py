from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

from core.models import Roster, Player, Letter, Position, Team
from core.data import *
from core.data_processor import *

from math import fsum
import numpy as np
import requests
import bs4


"""
Scrapes latest data from football database website,
updating the fantasy pts each player has. Manually
done by clicking a button.
"""
def update_fantasy_pts():
    
    for pos_key in interest_pos_keys:
        url = fantasy_pts_base_url % pos_key
        res = requests.get(url, headers={"User-Agent":"Mozilla/5.0"})
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # table with fantasy pts information
        table_block = soup.find('table', class_='statistics scrollable')
        data_rows = table_block.find_all('tr', class_=['row0 right', 'row1 right'])
        for row in data_rows:
            player_name = row.a.string
            fantasy_pts_block = row.find('td', class_='hilite')
            fantasy_pts = float(fantasy_pts_block.string)

            # assign fantasy pts to player
            p = Player.objects.filter(full_name=player_name, pos_key=pos_key)
            if p:
                player = Player.objects.get(full_name=player_name, pos_key=pos_key)
                player.fantasy_pts = fantasy_pts
                player.save()
            else:
                print("player not found")


"""
Searches fantasy pts earned by player by scraping webpage with
player stats from previous years
"""
def find_previous_years_stats(stats_url):
    res = requests.get(stats_url, headers={"User-Agent":"Mozilla/5.0"})

    # some web pages do not have previous fantasy statistics
    prev_fantasy_pts = {}
    if 'Fantasy Statistics' in res.text:
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        left_col_block = soup.find(id='leftcol')

        # table with previous years stats
        table = left_col_block.find_all('table', class_='statistics scrollable')[-1]

        data_rows = table.find_all('tr', class_=["row0 right", "row1 right"])
        prev_fantasy_pts = {}
        for row in data_rows:
            data_tags = row.find_all('td')
            year = data_tags[0].string
            fantasy_pts = float(data_tags[-1].string)
            prev_fantasy_pts[year] = fantasy_pts

    return prev_fantasy_pts



"""
Populate tables methods
"""

# delete all players and relationships with letters, teams and positions
def depopulate_all_tables():
    depopulate_players_table()
    depopulate_letters_table()
    depopulate_positions_table()
    depopulate_teams_table()

# scrape info and fill all players and relationships with letters, teams and positions
def populate_all_tables():
    populate_players_table()
    populate_letters_table()
    populate_positions_table()
    populate_teams_table()


"""
Players methods
"""

# delete all players from dB
def depopulate_players_table():
    players = Player.objects.all()
    for player in players:
        player.delete()

# scrape main info from football dB, assign data to new players
def populate_players_table():

    # web pages sort players by last name
    chars = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    urls = [players_base_url + "?letter=" + str(c) for c in chars]

    for url in urls:
        letter_char = url[-1]
        res = requests.get(url, headers={"User-Agent":"Mozilla/5.0"})
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        tr_blocks = soup.find_all('div', class_='tr')
        for block in tr_blocks:
            children = block.contents

            name = children[0].string
            last_name = name.split(",")[0]
            first_name = name.split(",")[1][1:]
            full_name = first_name + " " + last_name
            stats_url = base_url + children[0].a['href']

            pos_key = children[1].string

            if pos_key in interest_pos_keys:
                team_name = children[2].string
                college = children[3].string

                player = Player.objects.create(letter_char=letter_char, last_name=last_name, first_name=first_name, full_name=full_name, stats_url=stats_url, pos_key=pos_key, team_name=team_name, college=college)
                player.save()