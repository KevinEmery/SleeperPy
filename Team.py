class Team:
    def __init__(self, user, players):
        self.owner = user
        self.name = user.team_name
        self.players = players

    def get_team_size(self):
        return len(self.players)

    # Returns the number of offensive players
    def get_offensive_player_count(self):
        count = 0
        for player in self.players:
            if player.isOffensive():
                count += 1

        return count

    # Returns the number of defensive players on the team
    def get_defensive_player_count(self):
        count = 0
        for player in self.players:
            if player.isDefensive():
                count += 1

        return count

    # Returns the number of players at the specified position
    def get_count_at_position(self, position):
        count = 0
        for player in self.players:
            if player.position == position:
                count += 1

        return count

    # Returns the average age of every player at the specified position
    def get_average_age_at_position(self, position):
        count = 0
        ageSum = 0
        for player in self.players:
            if player.position == position:
                count += 1
                ageSum += player.age

        if count > 0:
            return ageSum / count
        else:
            return 0
