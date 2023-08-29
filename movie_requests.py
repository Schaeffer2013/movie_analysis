import requests
from keys import api_key
import csv
import re
import pandas as pd


csv_data = pd.read_csv("oscar_winners.csv")
csv_id = csv_data['IMDB']

def movie_res():
    with open('oscar_winners.csv', 'a') as csvfile:
            rows = csv.DictReader(csvfile)
            headers = ['Movie Title', 'Runtime', 'Genre', 'Award Wins', 'Award Nominations', 'Box Office']

            with open('movies.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(headers)

            for row in rows:
                res = requests.get(f"http://www.omdbapi.com?apikey={api_key}&i={movie_id}")
                api_data = res.json() 
                movie_id = int(api_data['imdbID'])
                title = str(api_data['Title'])
                time = int(api_data['Runtime'])
                genre = str(api_data['Genre'].split(", "))
                wins = int(api_data['Awards'])
                noms = int(api_data['Awards'])
                office = int(api_data['BoxOffice'])
            


                info = [title, time, genre, wins, noms, office]
  


