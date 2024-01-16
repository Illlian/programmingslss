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
print(ds)
