# Spotify data analizer
# Iliia Nyshpor
# Date: 16.01.24

import csv

def find_all_songs(artists: str) -> list:
    """A function that finds all the songs by a specific artist"""

    with open("./spotify.csv") as f:
        csv_r = csv.DictReader(f)

        # ds = []
        s = []
        for line in csv_r:
            # print(line)
            if artists.lower() in line["artist"].lower():
                s.append(
                   (line["artist"], line["song_title"], line["danceability"])
                )
        return s
       
drake_songs = find_all_songs("Drake")
# for s in drake_songs:
#     print(s)
# print(drake_songs)


# Version 0.1
# Get all the songs by Drake from the data list
with open("./spotify.csv") as f:
    # ---- Look for all songs performed by Drake
    #      Use linear search
    # Create a csv reader object
    csv_reader = csv.DictReader(f)

    # Create a list to store all Drake's songs
    drake_songs = []

    # for every song in the .csv file
    for line in csv_reader:
        if "drake" in line["artist"].lower():
            # add it to the Drake's songs list
            drake_songs.append(
                (line["artist"], line["song_title"], line["danceability"])
            )

# for song in drake_songs:
#     print(song)


# Sorting songs by danceability
# --- Sorting Algorithm (lowest to highest)
# --- Selection Sort

# Starting at the beginning of the list moving to the end
for i in range(len(drake_songs)):
    # Set the current item to the smallest value
    smallest_danceability = drake_songs[i][-1]
    smallest_index = i

    # For the rest of the list
    for j in range(i + 1, len(drake_songs)):
        # Check to see if this is smaller
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
                