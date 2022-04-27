from PlayerReader import PlayerReader
from player import Player

class PlayerStats:
    def __init__(self, reader):
        #reader = PlayerReader()
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team_filter(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )
        return list(players_of_team)

    def nationality_filter(self, chosen_nationality):
        players_of_natio = filter(
            lambda player: player.nationality == chosen_nationality,
            self._players
        )
        return list(players_of_natio)