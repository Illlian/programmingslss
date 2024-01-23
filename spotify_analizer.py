# Spotify data analizer
# Iliia Nyshpor
# Date: 16.01.24

import csv

def find_all_songs(artists: str) -> list:
    """A function that finds all the songs by a specific artist"""

    with open("./spotify.csv") as f:
        csv_r = csv.DictReader(f)

        # ds = []
        songs = []
        for line in csv_r:
            # print(line)
            if artists.lower() in line["artist"].lower():
                songs.append(
                   (line["artist"], line["song_title"], line["danceability"])
                )
        return songs
       
drake_songs = find_all_songs("Drake")
# for s in drake_songs:
#     print(s)
# print(drake_songs)


# Version 0.1
# Get all the songs by Drake from the data list
# ---- Look for all songs performed by Drake
    #      Use linear search
    # Create a csv reader object

with open("./spotify.csv") as f:
    csv_reader = csv.DictReader(f)

    drake_songs = []

    for line in csv_reader:
        if "drake" in line["artist"].lower():
            drake_songs.append(
                (line["artist"], line["song_title"], line["danceability"])
            )

# for song in drake_songs:
#     print(song)


# Sorting songs by danceability
# --- Sorting Algorithm (lowest to highest)
# --- Selection Sort


for i in range(len(drake_songs)):
    # Set the current item to the smallest value
    smallest_danceability = drake_songs[i][-1]
    smallest_index = i

    for j in range(i + 1, len(drake_songs)):
      
        if drake_songs[j][-1] < smallest_danceability:
            smallest_danceability = drake_songs[j][-1]
            smallest_index = j

    # Swap the current position with the smallest number we found
    drake_songs[i], drake_songs[smallest_index] = (
        drake_songs[smallest_index],
        drake_songs[i],
    )
    
print("--- Sorted Drake Songs by Danceability")
for song in drake_songs:
    print(f"{song[1]}:\t\t{song[2]}")


 # Task #2
 # Print all the songs that have danceability >= 0.6

    for song in drake_songs:
            # Alt version: 
            # if float(song[-1]) >= 0.6
            if float(line["danceability"]) >= 0.6:
               print(song)
                