class Team:
    def __init__(self, user, players):
        self.owner = user
        self.name = user.team_name
        self.players = players

    def getTeamSize(self):
        return len(self.players)

    # Returns the number of offensive players
    def getOffensivePlayerCount(self):
        count = 0
        for player in self.players:
            if player.isOffensive():
                count += 1

        return count

    # Returns the number of defensive players on the team
    def getDefensivePlayerCount(self):
        count = 0
        for player in self.players:
            if player.isDefensive():
                count += 1

        return count

    # Returns the number of players at the specified position
    def getCountAtPosition(self, position):
        count = 0
        for player in self.players:
            if player.position == position:
                count += 1

        return count

    # Returns the average age of every player at the specified position
    def getAverageAgeAtPosition(self, position):
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
