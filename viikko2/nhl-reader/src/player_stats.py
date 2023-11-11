class PlayerStats:
    def __init__(self, player_reader):
        self.reader = player_reader
        self.players = self.reader.get_players()

    def top_scores_by_nationality(self, nat):
        def filter_nationality(player):
            return True if player.nationality == nat else False

        filtered_players = filter(filter_nationality, self.players)
        return sorted(filtered_players, key=lambda player: player.points, reverse=True)
