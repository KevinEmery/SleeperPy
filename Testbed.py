from SleeperPy import SleeperPy

LEAGUE_ID = int(open("data/league_id.txt", "r").read())

api = SleeperPy("data/player_data.txt")
league = api.get_league(LEAGUE_ID)

for team in league.teams:
    print(team.owner.display_name + " - " + str(team.get_average_age_at_position("QB")))
