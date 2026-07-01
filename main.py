# import requests
# from bs4 import BeautifulSoup

# url = "http://example.com"

# response = requests.get(url)

# soup = BeautifulSoup(requests.text,"html.parser")

# print(soup.title.text)

from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/news")
def get_news(page: int = 1, limit:int = 5 ):
    url = "https://indianexpress.com/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    title = []

    for item in soup.find_all("a",class_="topblockNews__sidebarLink"):
        title.append(item.text)

    start = (page - 1) * limit
    end = start + limit

    return{
        "news":title[start:end],
        "page":page,
        "limit":limit,
        "total":len(title)
    }