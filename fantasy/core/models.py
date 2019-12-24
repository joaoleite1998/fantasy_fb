from django.db import models
from django.contrib.auth.models import User

from core.data import team_abbr

# Create your models here.

"""
Player model
Contains main information about player
letter_char 
"""
class Player(models.Model):
    objects = models.Manager()
    letter_char = models.CharField(max_length=1)
    last_name = models.CharField(max_length=30)     # first letter of player's last name
    first_name = models.CharField(max_length=30)    # player's first name
    full_name = models.CharField(max_length=61)     # player's last name
    stats_url = models.CharField(max_length=100)    # url with player's previous fantasy stats 

    pos_key = models.CharField(max_length=2)        # key of player's position (ex: QR for quarterback)
    team_name = models.CharField(max_length=30)     # player's nfl team
    college = models.CharField(max_length=30)       # college player attended
    fantasy_pts = models.FloatField(default=0.0)    # current number of fantasy pts for 2019 season
    available = models.BooleanField(default=True)   # bool if player has been drafted

    def __str__(self):
        return "%s, %s, %s, %s" % (self.last_name, self.first_name, self.pos_key, team_abbr[self.team_name])

    class Meta:
        ordering = ['last_name']

"""
Letter A-Z that has relationship with all player who's last name start with the letter
"""
class Letter(models.Model):
    objects = models.Manager()
    letter_char = models.CharField(max_length=1)    
    players = models.ManyToManyField(Player)

    class Meta:
        ordering = ['letter_char']

"""
Football position that has relationship with all players who play in that position
"""
class Position(models.Model):
    objects = models.Manager()
    pos_key = models.CharField(max_length=2)
    players = models.ManyToManyField(Player)

    class Meta:
        ordering = ['pos_key']

"""
NFL team that has relationship with all players who play in that team
"""
class Team(models.Model):
    objects = models.Manager()
    team_key = models.CharField(max_length=3)
    team_name = models.CharField(max_length=30)
    players = models.ManyToManyField(Player)

    class Meta:
        ordering = ['team_key']

"""
Roster owned by fanstasy user that contains the ids of all players user has drafted.
User can draft one quarterback, two running backs, three wide receivers, one tight end
and one other play of any position
"""
class Roster(models.Model):
    objects = models.Manager()
    owner_id = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)

    qb_id = models.IntegerField(default=0)
    rb_one_id = models.IntegerField(default=0)
    rb_two_id = models.IntegerField(default=0)
    wr_one_id = models.IntegerField(default=0)
    wr_two_id = models.IntegerField(default=0)
    wr_three_id = models.IntegerField(default=0)
    te_id = models.IntegerField(default=0)
    flex_id = models.IntegerField(default=0)

    def __str__(self):
        return "%s, %s" % (self.owner_id, self.created_at)

    # checks if all roster has been fill
    def __bool__(self):
        return not (qb_id == 0 or
                    rb_one_id == 0 or
                    rb_two_id == 0 or 
                    wr_one_id == 0 or 
                    wr_two_id == 0 or 
                    wr_three_id == 0 or
                    te_id == 0 or
                    flex_id == 0)

    def __iter__(self):
        return iter([self.qb_id, self.rb_one_id, self.rb_two_id, self.wr_one_id, self.wr_two_id, self.wr_three_id, self.te_id, self.flex_id])

    class Meta:
        ordering = ['owner_id']