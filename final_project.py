# final project

# Song Recommender
# this program scrapes Wikipedia's "List of Billboard Hot 100 number ones of 2023"
# and compiles the list of top songs this year into a dataframe then creates csv
# then imports data from csv and compiles into a dictionary
# the program recommends you a song based on a genre you input
# the user input will access the dictionary
# each song will be appended to a list and exported as a text file 

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
for row in columnData: 
    # docstring
    # checklist item 6.3-4
    '''iterates through each row in the whole table, appends song title each time it loops through '''
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
    "Pop": [], # checklist 5.8-9 values in for loop below are appended to this string
    "Country": [],
    "Kpop": [],
    "Rap": [],
}

# adding values from billboard into dictionary
# checklist item 5.18-19
for key, values in songDict.items():
    '''if key matches specified number, songs from billboard are added to genre dictionary'''
    if key in {0,18}: # the best way to do this was manually input the keys of the christmas songs
        songGenre["Christmas"].append(values) # the rest of these work the same for each key in genre dictionary
    elif key in {1, 2, 3, 6, 7, 12, 15 ,16}: 
        songGenre["Pop"].append(values) # checklist 5.8-9
    elif key in {4, 9, 10, 11}:
        songGenre["Country"].append(values)
        print(type(values))
    elif key in {5, 8}:
        songGenre["Kpop"].append(values)
    elif key in {13, 14}:
        songGenre["Rap"].append(values)
print(songGenre)

# empty list to add users given songs to
playlist = []

# ask for user input for genre
# checklist item 3.19
adding = input("Would you like to keep adding songs?\nYes\nNo\n")

while adding == "Yes":
    genre = input("What genre do you prefer?\n1: Christmas\n2: Pop\n3: Country\n4: Kpop\n5: Rap\nStop: Ready to create playlist.\n")
    
    '''returns random value from inputed genre'''
    if genre == "1":
        christmasResult = songGenre.get("Christmas", []) # gets values from key "christmas" ingenre dictionary
        randomChristmas = random.choice(christmasResult) # picks random song from the values
        print(randomChristmas)
        playlist.append(randomChristmas) # appends that song into the playlist
    elif genre == "2":
        popResult = songGenre.get("Pop", [])
        randomPop = random.choice(popResult)
        print(randomPop)
        playlist.append(randomPop)
    elif genre == "3":
        countryResult = songGenre.get("Country", [])
        randomCountry = random.choice(countryResult)
        print(randomCountry)
        playlist.append(randomCountry)
    elif genre == "4":
        kpopResult = songGenre.get("Kpop", [])
        randomKpop = random.choice(kpopResult)
        print(randomKpop)
        playlist.append(randomKpop)
    elif genre == "5":
        rapResult = songGenre.get("Rap", [])
        randomRap = random.choice(rapResult)
        print(randomRap)
        playlist.append(randomRap)
    elif genre == "Stop": # if user wants to stop adding songs
        print("Songs chosen. Your playlist is being created.")
        
        # remove playlist duplicates
        # checklist item 5.11
        for item in playlist: # iterates through songs in playlist
            while playlist.count(item) > 1: # if there is more than one of the same iten
                playlist.remove(item) # that item is removed from playlist

        print(playlist)
        break
    else:  
        # raise syntax error for possible misspellings
        # checklist item 4.9
        raise SyntaxError("There is a misspelling")

            
if adding == "No":
    print("Songs chosen. Your playlist is being created.")

    # remove playlist duplicates (same as above)
    for item in playlist:
            while playlist.count(item) > 1:
                playlist.remove(item)

# write out playlist to a new file
# checklist item 3.20
with open('/Users/naobae/Library/FinalProject/playlist.txt', 'w') as f:
    print(playlist, file = f)