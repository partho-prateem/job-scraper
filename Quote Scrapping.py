import requests
from bs4 import BeautifulSoup
import csv
pgno=1
with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer=csv.writer(f)
    writer.writerow(["Quote","Author"])
    while True:
        url= f"https://quotes.toscrape.com/page/{pgno}"
        source=requests.get(url)
        if "No Quotes Found!" in source.text:
            break
        soup= BeautifulSoup(source.text, "lxml")
        quotes= soup.find_all('div', class_="quote")
        for q in quotes:
            quote= q.find('span', class_="text").text
            author = q.find('small', class_="author").text
            tags = q.find ('div', class_="tags").text.replace(' ', '')
            print("Quote:", quote)
            print("Author:", author)
            print(tags)
            writer.writerow([quote, author])
        pgno +=1
        
