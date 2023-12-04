class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.matches_won_p1 = 0
        self.matches_won_p2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.matches_won_p1 = self.matches_won_p1 + 1
        else:
            self.matches_won_p2 = self.matches_won_p2 + 1

    def draw_score(self, score):
        if score < 3:
            return f"{self.format_game_points(self.matches_won_p1)}-All"
        return "Deuce"

    def match_result(self):
        match_score_difference = self.matches_won_p1 - self.matches_won_p2

        if match_score_difference == 1:
            return "Advantage player1"
        elif match_score_difference == -1:
            return "Advantage player2"
        elif match_score_difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
    
    def format_game_points(self, score):
            match score:
                case 0:
                    return "Love"
                case 1:
                    return "Fifteen"
                case 2:
                    return "Thirty"
                case 3:
                    return "Forty"

    def game_score(self):
        score = f"{self.format_game_points(self.matches_won_p1)}-{self.format_game_points(self.matches_won_p2)}"
        return score

    def get_score(self):
        score_string = ""

        if self.matches_won_p1 == self.matches_won_p2:
            score_string = self.draw_score(self.matches_won_p1)
        elif self.matches_won_p1 >= 4 or self.matches_won_p2 >= 4:
            score_string = self.match_result()
        else:
            score_string = self.game_score()

        return score_string
