from SleeperPy import SleeperPy

LEAGUE_ID = int(open("data/league_id.txt", "r").read())

api = SleeperPy("data/player_data.txt")
league = api.getLeague(LEAGUE_ID)

for team in league.teams:
    print(team.owner.display_name)
    print(team.getAverageAgeAtPosition("LB"))
