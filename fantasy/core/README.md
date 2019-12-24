This is a basic fantasy football app which collects data directly from the football
database website. Third party packages Beautiful soup4, request, Django and numpy
must be installed to use this application. First party packages math and datetime are
also used.

Users can create a login and draft players based on their availability
(they become unavailable if another user drafts them).

To run the app, use the terminal to navigate to the root fantasy folder (where manage.py is located) and run

python manage.py runserver

The following message will appear. From here, simply click on the link, which will take you to 
the splash page

Starting development server at http://127.0.0.1:8000/ 

After logging in you are directed to the homepage, which displays your current roster
and contains a few links to other parts of the app. 

It is necessary to populate the database with current nflplayers after creating your
login. This is done simply by clicking on the populate database button on the top-right
of the home page and takes are 2 minutes. Note that this only needs to be done once 
after creating your username

It is also necessary update the player statistics by clicking on the update statistics
button also on the top-right of the home page. These statistics should be updated as 
new NFL games take place in the current season. Ideally this can be automated so that
a script runs every week and the user doesn't have to manually do this.

In the homepage you have the option of drafting a new player to an empty spot or droping a 
currently filled spot. There is no deadline to drafting and dropping, but if another user
drafts a player before you, then you can no longer draft that player, unless the player
is then dropped. When choosing to draft a new player, the app will take you to a new page 
with a list of currently available players in the respective position, together with their
fantasy points in the current season.

From the home page you also have the option of search all players and analyzing their previous
statistics. This is done by clicking on the Player Stats link on the homepage, which 
directs you to another page where you can find player by last name, position or team, or 
simply get a list of all the players. For each player on the list presented you have the option of clicking on a "View Stats" link, which displays their fantasy pts earned on previous seasons. 


