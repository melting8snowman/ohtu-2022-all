import requests
from player import Player
from PlayerReader import PlayerReader
from PlayerStats import PlayerStats

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    #print("Players from team Dallas")
    #players = stats.team_filter("DAL")

    #print("Players from nationality Finland")
    #players = stats.nationality_filter("FIN")

    print("Top Scorers of nationality")
    players = stats.nationality_filter("FIN")

    for player in players:
        print(player)

        
if __name__ == "__main__":
    main()
