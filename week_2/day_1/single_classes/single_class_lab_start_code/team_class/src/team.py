# TESTS
class Team:

    def __init__(self, team_name, team_players, team_coach):
        self.name = team_name
        self.players = team_players
        self.coach = team_coach
        self.points = 0

    def add_player(self, team_players):
        self.players.append(team_players)


    def has_player(self, player_to_find):
        for player in self.players:
            if player == player_to_find:
                return True
        return False

    def play_game(self, result):
        if result == True:
            self.points += 3
         
