import unittest
from statistics import Statistics
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

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # stub
        self.statistics = Statistics(PlayerReaderStub())
    
    def test_team_stat_search_single(self):
        team = self.statistics.team("PIT")
        self.assertEqual(1, len(team))
        names = ["Lemieux"]
        self.assertEqual(names, sorted(p.name for p in team))

    def test_team_stat_search_multi(self):
        team = self.statistics.team("EDM")
        self.assertEqual(3, len(team))
        names = ["Gretzky", "Kurri", "Semenko"]
        self.assertEqual(names, sorted(p.name for p in team))



    def test_top_2(self):
        players = self.statistics.top_scorers(1)
        self.assertEqual(2, len(players))
        self.assertEqual("Gretzky", players[0].name)
        self.assertEqual("Lemieux", players[1].name)


    def test_player_search(self):
        player = self.statistics.search("Semenko")
        self.assertEqual("EDM", player.team)
        self.assertEqual(4, player.goals)

    def test_negat_player_search(self):
        player = self.statistics.search("Aho")
        self.assertEqual(None, player)

