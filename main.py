# importing all important libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# creating empty list to store data later on
rating_list = []
title_list = []
price_list = []
availablity = []

# parsing the whole website as an html using html.parser and requests library
url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
rating = soup.find_all(name="p", class_="star-rating")

# fetching the ratings
for stars in rating:
    rating_list.append(stars.get("class")[1])

# fetching the titles
titles = soup.select("h3 a")
for title in titles:
    title_list.append(title.text)

# fetching the prices
prices = soup.find_all(name="p", class_="price_color")
for price in prices:
    price_list.append(float(price.text.strip("£")))

# fetching the status
status = soup.find_all(name="p", class_="availability")
for stat in status:
    availablity.append(stat.text.strip())

# creating a dictionary data structure
dict = {'Title': title_list, 'Rating' : rating_list, 'Price': price_list, 'Availabity': availablity}

# converting the dictionary to dataframe
df = pd.DataFrame(dict)

# using pandas to convert the dataframe to csv
df.to_csv('book_store.csv')

# printing the dataframe
print(df)
