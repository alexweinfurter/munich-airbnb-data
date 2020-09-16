import requests
import re
import os
from pathlib import Path
from bs4 import BeautifulSoup

INSIDE_AIRBNB = "http://insideairbnb.com/get-the-data.html"
RAW_DATA_FOLDER = "data/raw"
CITY = "munich"
PROJECT_FOLDER = Path(__file__).parent.parent


def parse_urls(url, city):
    """Gets all urls related to the city."""
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    html_table = " ".join(["table table-hover table-striped", city])
    table = soup.find_all('table', class_=html_table)
    urls = []
    for element in table:
        for a in element.find_all("a", href=True):
            urls.append(a["href"])
    return urls

def filter_urls(urls):
    """Selects urls of relevant files."""
    patterns = ["listings.csv.gz","calendar.csv.gz","reviews.csv.gz", "neighbourhoods"]
    relevant = filter(lambda x: any([(p in x ) for p in patterns]), urls)
    return relevant

def download_files(urls):
    """Downloads all files."""
    for url in urls:
        match = re.search(r"\d{4}-\d{2}-\d{2}", url) # extract date year-month-day
        date = match.group()

        folder = (PROJECT_FOLDER / RAW_DATA_FOLDER / CITY / date).resolve()

        Path(folder).mkdir(parents=True, exist_ok=True)

        file_name = url.split("/")[-1] # gets str behind last /-sign
        path = (folder / file_name).resolve()

        print("CREATE FILE:")
        print(path)
        with open(path, "wb") as file:
            req = requests.get(url, allow_redirects=True) # download file
            file.write(req.content)
        print("DONE")



urls = parse_urls(INSIDE_AIRBNB, CITY)
filtered = list(filter_urls(urls))
download_files(filtered)


    
    

    

