# final project

# Song Recommender
# this program imports a database of songs from the Billboard Hot 100 charts
# data from Billboard will be compiled into a dictionary
# then it recommends you a song based on a genre you input
# the user input will access the dictionary
# after you choose several songs, that data will be appended to a list
# and the program will create a file including a personalized playlist

# webscrape for a table of information (10.1)
# store data in dictionary (5.15-9)
# JSON is represented as dictionary before stringified

import pandas as pd
import random

# import csv file
# checklist item 8.2
billboard = pd.read_csv(r'/Users/naobae/Library/FinalProject/Billboard100.csv')
print(billboard)

# converting into string
outerDict = billboard.to_dict()
songDict = outerDict['Song']

# create a dictionary of genres
# checklist item 5.15
songGenre = {
    "Christmas": [], # values are blank to append songs from billboard
    "Pop": [],
    "Country": [],
    "Kpop": [],
    "Rap": [],
}

# adding values from billboard into dictionary
for key, values in songDict.items():
    if key in {0,18}: # the best way to do this was manually input the keys of the christmas songs
        songGenre["Christmas"].append(values) # if key matches specified number, songs from billboard are added to genre dictionary
    elif key in {1, 2, 3, 6, 7, 12, 15 ,16}: # the rest of these work the same for each key in genre dictionary
        songGenre["Pop"].append(values)
    elif key in {4, 9, 10, 11}:
        songGenre["Country"].append(values)
    elif key in {5, 8}:
        songGenre["Kpop"].append(values)
    elif key in {13, 14}:
        songGenre["Rap"].append(values)
print(songGenre)
    
# an ask user if they want multiple songs from an artist
# have the value as a list and append/remove items (5.9,11)

# can make billboard.py into a module to import (3.17)

# can write the results out to file, like make them a list of songs (3.20)
# raise error for unknown genre (4.9)
# can you make pandas data into dictionary?
# need to learn licensing
# once user has curated a playlist, use numpy to calculate how many songs each time add?
    