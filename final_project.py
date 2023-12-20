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

# billboard

# this program scrapes Wikipedia's "List of Billboard Hot 100 number ones of 2023"
# and compiles the list of top songs this year into a dataframe

from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import random

# using beautifulsoup to parse website content
# checklist item 10.1-2
url = "https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number_ones_of_2023"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# find track names
table = soup.find('table', class_ = 'wikitable sortable plainrowheaders') # isolate tracklist table
body = table.find('tbody') # going down in tree
columnHeaders = body.find('tr') # finds row of column headers (no., song, artist, etc.)
indivColumn = columnHeaders.find_all('th')[2] # isolates song column only
titles = [title.text.strip() for title in indivColumn] # formats title into text, strip() gets rid of extra indent

# using pandas to create dataframe
df = pd.DataFrame(columns = titles) 

# going down in tree
columnData = body.find_all('tr')[1:]

# finds song in specified column from each row
for row in columnData: # iterates through each row in the whole table, appends song title each time it loops through 
    songTitle = row.find('a', title=re.compile(r'.*')) # finds song title
    
    # convert titles to text and append to dataframe
    if songTitle:
        indivRowData = songTitle.text # converts each title to text
        df.loc[len(df.index)] = [indivRowData] # checks how many columns in dataframe each loop and puts data in next row

print(df) # print dataframe

# write dataframe into csv
# checklist item 8.4
df.to_csv(r'/Users/naobae/Library/FinalProject/Billboard100.csv', index = False)

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