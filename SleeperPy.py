# Used for the API calls
import requests

# Used to check for the existence of the player data
import os.path

# Used for converting the JSON response for the player data to string
import json

# Import the custom classes we've defined
from User import User
from Team import Team
from Player import Player
from League import League


class SleeperPy:
    # Base URLs used as a part of the API requests
    _get_user_base_url = "https://api.sleeper.app/v1/user/"
    _get_league_base_url = "https://api.sleeper.app/v1/league/"
    _get_players_url = "https://api.sleeper.app/v1/players/nfl"

    def __init__(self, filename):
        self.player_map = {}

        # Check to see if we should be re-creating the player file
        if self._shouldCreatePlayerFile(filename):
            self._createPlayerFile(filename)

        # Read the player file from disk, placing the data into the dictionary
        with open(filename, "r") as file:
            player_info = json.loads(file.read())
            for player_id in player_info:
                player_data = player_info[player_id]

                # Parse the first/last name into a single string
                player_name = player_data["first_name"] + " " + player_data["last_name"]

                # Parse the other player data, allowing for "none"
                player_pos = self._parsePlayerPosition(player_data["fantasy_positions"])
                player_age = self._parsePlayerAge(player_data["age"])

                self.player_map[player_id] = Player(player_name, player_pos, player_age)

    # Determines whether or not we should create/recreate the player data file
    def _shouldCreatePlayerFile(self, filename):
        return not os.path.exists(filename)

    # Deletes and creates the player data file
    def _createPlayerFile(self, filename):
        # We may be re-creating it because the file is too old, so check if we need to delete first
        if os.path.exists(filename):
            print("Deleting existing player file")
            os.remove(filename)

        print("Creating player data file")
        # Create the intermediate directories if they don't already exist
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))

        # Having cleared the way, prepare to create the player file
        with open(filename, "w") as file:
            r = requests.get(self._get_players_url)

            file.write(json.dumps(r.json()))

    # Parse their fantasy position from the list provided, otherwise returning none
    # The main reason we have to handle "None" is because the coaches are in this data
    def _parsePlayerPosition(self, raw_fantasy_positions):
        try:
            player_pos = raw_fantasy_positions[0]
        except TypeError:
            player_pos = "None"

        return player_pos

    # Parse their player age to an int from the string provided, default 0
    # The main reason we have to handle this is because the coaches are in this data with age "None"
    def _parsePlayerAge(self, raw_age):
        try:
            player_age = int(raw_age)
        except TypeError:
            player_age = 0

        return player_age

    # Prints out the metadata for the given league
    def getLeague(self, league_id):
        r = requests.get(self._get_league_base_url + str(league_id))
        league_json = r.json()
        league_name = league_json["name"]

        # Retrieve the list of users
        users = self.getUsersInLeague(league_id)

        # Retrieve the rosters from the server
        r = requests.get(self._get_league_base_url + str(league_id) + "/rosters")
        teams = []
        for roster in r.json():
            # Build the player list for each team
            players = []
            for player in roster["players"]:
                players.append(self.getPlayer(player))

            teams.append(Team(users[roster["owner_id"]], players))

        return League(league_name, teams)

    # Returns a list of all of the users within the given league ID
    def getUsersInLeague(self, league_id):
        r = requests.get(self._get_league_base_url +
                         str(league_id) + "/users")
        users = {}
        for data in r.json():
            user = User(data)
            users[user.user_id] = user

        return users

    # Retrieve a specific player from the map, otherwise returning unknown
    def getPlayer(self, player_id):
        # Retrieve the player from the in-memory dictionary
        if player_id in self.player_map:
            return self.player_map[player_id]

        print("Found unknown player_id " + player_id)
        return Player("Unknown", "Unknown", 0)
