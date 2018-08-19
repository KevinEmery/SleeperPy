# Used to suppress specific exceptions, as a compact try/catch
from contextlib import suppress
# Used for the API calls
import requests
# Used for converting the JSON response for the player data to string
import json

class User:

    # Base URLs used as a part of the API requests
    _get_user_base_url = "https://api.sleeper.app/v1/user/"


    user_id = ""
    username = ""
    display_name = ""
    team_name = ""

    def __init__(self, json):
        self.display_name = json["display_name"]
        self.user_id = json["user_id"]

        # Both of these fields aren't always available, but we're going to try to read them anyway
        with suppress(KeyError):
            self.username = json["username"]
        with suppress(KeyError):
            self.team_name = json["metadata"]["team_name"]


    @classmethod
    def getUser_byUsername(self,username):
        r = requests.get(self._get_user_base_url + username)
        data = r.json()
        return self(data)

    @classmethod
    def get_User_byID(self,user_id):
        r = requests.get(self._get_user_base_url + str(user_id))
        data = r.json()
        return self(data)
