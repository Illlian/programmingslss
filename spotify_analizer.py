# Spotify data analizer
# Iliia Nyshpor
# Date: 16.01.24

# Version 0.1
# Get all the songs by Drake from the data list

import csv

with open("./spotify.csv") as f:
    csv_r = csv.DictReader(f)

    ds = []

    for line in csv_r:
        # print(line)

        if "drake" in line["artist"].lower():
            ds.append(
                (line["artist"], line["song_title"], line["danceability"])
            )
# print(ds)

# Task #2
# Print all the songs that have danceability >= 0.6

with open("./spotify.csv") as f:
    csv_r = csv.DictReader(f)

    dnc = []

    for line in csv_r:
        if float(line["danceability"]) >= 0.6:
            dnc.append(
                (line["artist"], line["song_title"], line["danceability"])   
            )
print(dnc)