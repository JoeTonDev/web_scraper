import requests
from bs4 import BeautifulSoup

url="https://www.imdb.com/chart/top"
response = requests.get(url)

if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, "html.parser")
    movie_containers = soup.find_all("td", class_="titleColumn")
    movies=[]
    for container in movie_containers:
      title = container.a.text
      year = container.span.text[1:1]
      movie = {"title": title, "year": year}
      movies.append(movie)
      
      for i, movie in enumerate(movies[:10]):
        print(i+1, movie["title"], movie["year"])
else:
    print("Failed to retrieve data from IMDB")