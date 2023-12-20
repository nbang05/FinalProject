Song Recommender

This project imports a database of songs from a Wikipedia page including the Billboard Hot 100 chart 2023. Data from Billboard is compiled into a dictionary and organized by genre, then the program will ask to input a genre out of the five listed. The user input will access the dictionary and output a randomized song from that genre. After choosing several songs, that data will be appended to a list, and the program will create a file including a personalized playlist.

User Requirements

Installation

Install Python

Additionally, import the following:

from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import random

Running the Script

The main script of the project is final_project.py and can be run from the command line with the command:

python final_project.py

License

This project is licensed under the MIT License (see LICENSE.md)