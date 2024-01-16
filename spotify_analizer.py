# Spotify data analizer
# Iliia Nyshpor
# Date: 16.01.24

# Version 0.1
# Get all the songs by Drake from the data list

import csv

def find_all_songs(artists: str) -> list:

    with open("./spotify.csv") as f:
        csv_r = csv.DictReader(f)

        # ds = []
        s = []
        for line in csv_r:
            # print(line)
            if artists.lower() in line["artist"]:
                s.append(
                   (line["artist"], line["song_title"], line["danceability"])
                )
        return s

            # if "drake" in line["artist"].lower():
            #     ds.append(
            #         (line["artist"], line["song_title"], line["danceability"])
            #     )
    # print(ds)

    # # Task #2
    # # Print all the songs that have danceability >= 0.6

    # with open("./spotify.csv") as f:
    #     csv_r = csv.DictReader(f)

    #     dnc = []

    #     for line in csv_r:
    #         # Alt version: 
    #         # if float(song[-1]) >= 0.6
    #         if float(line["danceability"]) >= 0.6:
    #             dnc.append(
    #                 (line["artist"], line["song_title"], line["danceability"])   
    #             )
    # print(dnc)