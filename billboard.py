# billboard

# this program scrapes Wikipedia's "List of Billboard Hot 100 number ones of 2023"
# and compiles the list of top songs this year into a dataframe

from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

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






#################################################### for main code
# empty list to add users given songs to
playlistRecs = []

# ask for user input for genre
adding = input("Would you like to keep adding songs?\nYes\nNo\n")
if adding == "Yes":
    genre = input("What genre do you prefer?\n1: Christmas\n2: Pop\n3: Country\n4: Kpop\n5: Rap\n")
elif adding == "No":
    print("Songs chosen. Your playlist is being created.")

# return random value from inputed genre
if genre == "1":
    christmasResult = songGenre.get("Christmas", [])
    randomChristmas = random.choice(christmasResult)
    print(randomChristmas) 
