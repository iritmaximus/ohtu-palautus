import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_correct_name(self):
        result = self.stats.search("Kurri")
        self.assertEqual(result.name, "Kurri")
        self.assertEqual(result.team, "EDM")

    def test_search_incorrect_name(self):
        result = self.stats.search("Minä :)")
        self.assertEqual(result, None)


    def test_team_correct_team(self):
        result = self.stats.team("EDM")
        self.assertEqual(result[0].name, "Semenko")
        self.assertEqual(result[1].name, "Kurri")
        self.assertEqual(result[2].name, "Gretzky")

    def test_top_right_players(self):
        result = self.stats.top(3)
        self.assertEqual(result[0].name, "Gretzky")
        self.assertEqual(result[1].name, "Lemieux")
        self.assertEqual(result[2].name, "Yzerman")

    def test_top_with_points_parameter(self):
        result = self.stats.top(3, 1)
        self.assertEqual(result[0].name, "Gretzky")
        self.assertEqual(result[1].name, "Lemieux")
        self.assertEqual(result[2].name, "Yzerman")

    def test_top_with_goals_parameter(self):
        result = self.stats.top(3, 2)
        self.assertEqual(result[0].name, "Lemieux")
        self.assertEqual(result[1].name, "Yzerman")
        self.assertEqual(result[2].name, "Kurri")

    def test_top_with_assists_parameter(self):
        result = self.stats.top(3, 3)
        self.assertEqual(result[0].name, "Gretzky")
        self.assertEqual(result[1].name, "Yzerman")
        self.assertEqual(result[2].name, "Lemieux")

    def test_top_with_incorrect_parameter(self):
        result = self.stats.top(3, 20)
        self.assertEqual(result[0].name, "Gretzky")
        self.assertEqual(result[1].name, "Lemieux")
        self.assertEqual(result[2].name, "Yzerman")
