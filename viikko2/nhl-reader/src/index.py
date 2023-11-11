import requests
from player_reader import PlayerReader
from player_stats import PlayerStats


URL = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"

def main():
    reader = PlayerReader(URL)
    stats = PlayerStats(reader)
    players = stats.top_scores_by_nationality("FIN")

    for player in players:
        print(player)


if __name__ == "__main__":
    main()
