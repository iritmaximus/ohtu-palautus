from enum import IntEnum

class SortBy(IntEnum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3


class StatisticsService:
    def __init__(self, reader):
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by_value=SortBy.POINTS):
        def sort_by_points(player): 
            return player.points
        def sort_by_goals(player):
            return player.goals
        def sort_by_assists(player):
            return player.assists

        match sort_by_value:
            case SortBy.POINTS:
                sorted_players = sorted(
                    self._players,
                    reverse=True,
                    key=sort_by_points
                )
            case SortBy.GOALS:
                sorted_players = sorted(
                    self._players,
                    reverse=True,
                    key=sort_by_goals
                )
            case SortBy.ASSISTS:
                sorted_players = sorted(
                    self._players,
                    reverse=True,
                    key=sort_by_assists
                )
            case _:
                sorted_players = sorted(
                    self._players,
                    reverse=True,
                    key=sort_by_points
                )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
