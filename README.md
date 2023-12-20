Song Recommender

This project imports a database of songs from a Wikipedia page including the Billboard Hot 100 chart 2023. Data from Billboard is compiled into a dictionary and organized by genre, then the program will ask to input a genre out of the five listed. The user input will access the dictionary and output a randomized song from that genre. Each randomized song will be appended to a playlist list and exported as a text file.

User Requirements

Installation

Install Python:

pip install python

Additionally, import the following:

from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import random

Running the Script

The project is final_project.py and can be run from the command line with the command: (checklist item 1.5)

python final_project.py

License

This project is licensed under the MIT License (see LICENSE.md)