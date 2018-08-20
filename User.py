# Used to suppress specific exceptions, as a compact try/catch
from contextlib import suppress
# Used for the API calls
import requests


class User:

    # Base URLs used as a part of the API requests
    _get_user_base_url = "https://api.sleeper.app/v1/user/"

    user_id = ""
    username = ""
    display_name = ""
    team_name = ""
    user_leagues_metadata = {}

    def __init__(self, json):
        self.display_name = json["display_name"]
        self.user_id = json["user_id"]

        # Both of these fields aren't always available, but we're going to try to read them anyway
        with suppress(KeyError):
            self.username = json["username"]
        with suppress(KeyError):
            self.team_name = json["metadata"]["team_name"]

        self.user_leagues_metadata = self.get_leagues()

    @classmethod
    def get_user_by_username(self, username):
        r = requests.get(self._get_user_base_url + username)
        data = r.json()
        return self(data)

    @classmethod
    def get_user_by_id(self, user_id):
        r = requests.get(self._get_user_base_url + str(user_id))
        data = r.json()
        return self(data)

    def get_leagues(self, sport="nfl", season=2018):
        r = requests.get(self._get_user_base_url + str(self.user_id) + "/leagues/" + sport + "/" + str(season))

        leagues = {}

        # Check for a successful response before parsing the body
        if (r.status_code >= 200 & r.status_code < 300):
            for league in r.json():

                league_id = league["league_id"]
                league_name = league["name"]
                leagues[league_id] = league_name

        return leagues
