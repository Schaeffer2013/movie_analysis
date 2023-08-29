import requests
from keys import api_key
import csv
import re


def movie_res():
    with open('oscar_winners.csv', 'r') as csvfile:
            rows = csv.DictReader(csvfile)
            headers = ['Movie Title', 'Runtime', 'Genre', 'Award Wins', 'Award Nominations', 'Box Office', 'Rated', 'Language','Director']
            movie_choices = [
                 "tt2278388",
                 "tt0109830",
                 "tt1375666",
                 "tt0120689",
                 "tt2380307"
            ]
            with open('movies.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(headers)

            for row in rows:
                csv_id = row['IMDB']
                res = requests.get(f"http://www.omdbapi.com?apikey={api_key}&i={csv_id}")
                api_data = res.json() 
                title = str(api_data['Title'])
                time = int(api_data['Runtime'])
                genre = str(api_data['Genre'].split(", "))
                awards = re.findall(r'\d+', api_data['Awards'])
                wins = int(awards[0]) if awards else 0
                noms = int(awards[1]) if len(awards) > 1 else 0
                office = int(api_data['BoxOffice', 0])
                rated = str(api_data['Rated'])
                lang = str(api_data['Language'].split(", "))
                director = str(api_data['Director'])
               


            
                info = [title, time, genre, wins, noms, office, rated, lang, director]
                
                with open('movies.csv', 'a', newline='', encoding='utf-8') as f:
                     writer = csv.writer(f)
                     writer.writerow([info])

movie_res()
  


