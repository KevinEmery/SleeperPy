# Used to suppress specific exceptions, as a compact try/catch
from contextlib import suppress


class User:
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
