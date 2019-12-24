"""
contains static data that is used in many parts of the app.
particularly useful are urls used in web scraping and abbreviations
for player teams and positions
"""

all_pos_abbr = {
    'C': 'Center',
    'DB': 'Defensive Back',
    'DE': 'Defensive End',
    'DL': 'Defensive Lineman',
    'DT': 'Defensive Tackle',
    'K': 'Kicker',
    'LB': 'Linebacker',
    'LS': 'Long snapper',
    'OG': 'Offensive Guard',
    'OL': 'Offensive Lineman',
    'OT': 'Offensive Tackle',
    'P': 'Punter',
    'QB': 'Quarterback',
    'RB': 'Running Back',
    'TE': 'Tight End',
    'WR': 'Wide Receiver',
}

pos_abbr = {
    'K': 'Kicker',
    'QB': 'Quarterback',
    'RB': 'Running Back',
    'TE': 'Tight End',
    'WR': 'Wide Receiver',
}

team_data = [
    ['ARI', 'Arizona', 'Cardinals', 'Arizona Cardinals'],
    ['ATL', 'Atlanta', 'Falcons', 'Atlanta Falcons'],
    ['BAL', 'Baltimore', 'Ravens', 'Baltimore Ravens'],
    ['BUF', 'Buffalo', 'Bills', 'Buffalo Bills'],
    ['CAR', 'Carolina', 'Panthers', 'Carolina Panthers'],
    ['CHI', 'Chicago', 'Bears', 'Chicago Bears'],
    ['CIN', 'Cincinnati', 'Bengals', 'Cincinnati Bengals'],
    ['CLE', 'Cleveland', 'Browns', 'Cleveland Browns'],
    ['DAL', 'Dallas', 'Cowboys', 'Dallas Cowboys'],
    ['DEN', 'Denver', 'Broncos', 'Denver Broncos'],
    ['DET', 'Detroit', 'Lions', 'Detroit Lions'],
    ['GB', 'Green Bay', 'Packers', 'Green Bay Packers', 'G.B.', 'GNB'],
    ['HOU', 'Houston', 'Texans', 'Houston Texans'],
    ['IND', 'Indianapolis', 'Colts', 'Indianapolis Colts'],
    ['JAC', 'Jacksonville', 'Jaguars', 'Jacksonville Jaguars', 'JAX'],
    ['KC', 'Kansas City', 'Chiefs', 'Kansas City Chiefs', 'K.C.', 'KAN'],
    ['LA', 'Los Angeles', 'Rams', 'Los Angeles Rams', 'L.A.'],
    ['MIA', 'Miami', 'Dolphins', 'Miami Dolphins'],
    ['MIN', 'Minnesota', 'Vikings', 'Minnesota Vikings'],
    ['NE', 'New England', 'Patriots', 'New England Patriots', 'N.E.', 'NWE'],
    ['NO', 'New Orleans', 'Saints', 'New Orleans Saints', 'N.O.', 'NOR'],
    ['NYG', 'Giants', 'New York Giants', 'N.Y.G.'],
    ['NYJ', 'Jets', 'New York Jets', 'N.Y.J.'],
    ['OAK', 'Oakland', 'Raiders', 'Oakland Raiders'],
    ['PHI', 'Philadelphia', 'Eagles', 'Philadelphia Eagles'],
    ['PIT', 'Pittsburgh', 'Steelers', 'Pittsburgh Steelers'],
    ['SD', 'San Diego', 'Chargers', 'San Diego Chargers', 'S.D.', 'SDG'],
    ['SEA', 'Seattle', 'Seahawks', 'Seattle Seahawks'],
    ['SF', 'San Francisco', '49ers', 'San Francisco 49ers', 'S.F.', 'SFO'],
    ['STL', 'St. Louis', 'Rams', 'St. Louis Rams', 'S.T.L.'],
    ['TB', 'Tampa Bay', 'Buccaneers', 'Tampa Bay Buccaneers', 'T.B.', 'TAM'],
    ['TEN', 'Tennessee', 'Titans', 'Tennessee Titans'],
    ['WAS', 'Washington', 'Redskins', 'Washington Redskins', 'WSH']
]

team_abbr = {
    'Arizona': 'ARI',
    'Atlanta': 'ATL',
    'Baltimore': 'BAL',
    'Buffalo': 'BUF',
    'Carolina': 'CAR',
    'Chicago': 'CHI',
    'Cincinnati': 'CIN',
    'Cleveland': 'CLE',
    'Dallas': 'DAL',
    'Denver': 'DEN',
    'Detroit': 'DET',
    'Green Bay': 'GB',
    'Houston': 'HOU',
    'Indianapolis': 'IND',
    'Jacksonville': 'JAC',
    'Kansas City': 'KC',
    'LA Chargers': 'LAC',
    'LA Rams': 'LA',
    'Miami': 'MIA',
    'Minnesota': 'MIN',
    'New England': 'NE',
    'New Orleans': 'NO',
    'NY Giants': 'NYG',
    'NY Jets': 'NYJ',
    'Oakland': 'OAK',
    'Philadelphia': 'PHI',
    'Pittsburgh': 'PIT',
    'San Francisco': 'SF',
    'Seattle': 'SEA',
    'Tampa Bay': 'TB',
    'Tennessee': 'TEN',
    'Washington': 'WAS'
}   

player_pos_keys = {
    'QB': 'QB',
    'RB1': 'RB',
    'RB2': 'RB',
    'WR1': 'WR',
    'WR2': 'WR',
    'WR3': 'WR',
    'TE': 'TE'
}

letter_chars = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

interest_pos_keys = ['QB', 'RB', 'WR', 'TE', 'K']

base_url = 'https://www.footballdb.com'

players_base_url = 'https://www.footballdb.com/players/current.html'

fantasy_pts_base_url = 'https://www.footballdb.com/fantasy-football/index.html?pos=%s&yr=2019&wk=all&rules=1'
