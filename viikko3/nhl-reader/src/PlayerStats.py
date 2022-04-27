from PlayerReader import PlayerReader
from player import Player

def points_first(player):
    return player.points, player.team

class PlayerStats:
    def __init__(self, reader):
        #reader = PlayerReader()
        self._players = reader.get_players()

    def team_filter(self, chosen_team):
        players_of_team = filter(
            lambda player: player.team == chosen_team,
            self._players
        )
        return list(players_of_team)

    def nationality_filter(self, chosen_nationality):
        players_of_natio = filter(
            lambda player: player.nationality == chosen_nationality,
            self._players
        )

        sorted_players = sorted(
            players_of_natio,
            reverse=True,
            key=points_first
        )
        return sorted_players
