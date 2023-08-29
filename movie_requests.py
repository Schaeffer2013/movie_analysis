import requests
from keys import api_key
import csv
import re


res = requests.get(f"http://www.omdbapi.com/?&apikey={api_key}")
data = res.json()
id = data['imdbID']
title = str(data['Title'])
time = int(data['Runtime'])
genre = str(data['Genre'])
wins = int(data['Awards'])
noms = int(data['Awards'])
office = int(data['BoxOffice'])
res = requests.get(f"http://www.omdbapi.com?i={id}&apikey={api_key}")
print(data)


headers = ['Movie Title', 'Runtime', 'Genre', 'Award Wins', 'Award Nominations', 'Box Office']
info = ['Movie Title', 'Runtime', 'Genre', 'Award Wins', 'Award Nominations', 'Box Office']

def movie_res():
    with open('oscar_winners.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerow(info)

  


