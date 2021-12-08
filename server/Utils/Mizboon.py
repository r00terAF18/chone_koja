from typing import Any
import requests
import json
from bs4 import BeautifulSoup as bs


class Mizboon:
    def __init__(self, link, price, title, city):
        self.link = link
        self.price_per_night = price
        self.title = title
        self.city = city
        self.BASE_URL = "https://mizboon.com"

    def __str__(self) -> str:
        return f"Room {self.title} with Stars {self.stars} at {self.link}"

    def __dict__(self) -> dict:
        return {
            "UID": self.id,
            "title": self.title,
            "link_to_site": self.link,
            "price_per_night": self.price_per_night,
            "rating": self.stars,
            "state": "",
            "city": self.city,
        }

    def setup(self) -> None:
        self._set_id()
        self._setup_data()
        # self._set_ppn()
        self._set_stars()
        # self._set_title()

    def _set_id(self):
        self.id = self.link.split("/")[4].split(".")[0]

    def _setup_data(self):
        response = requests.get(self.link).content.decode("utf-8")
        # with open('index.html', "r") as f:
        #     response = f.read()
        #     f.close()
        self.data = bs(response, "html5lib")

    def _set_ppn(self):
        ppn = 0
        li = self.data.find("div", attrs={"class": "rm_si_price"})
        if li is not None:
            ppn = (
                li.find("span")
                .text.strip()
                .replace("تومان", "")
                .replace("از", "")
                .strip()
            )
        self.price_per_night = ppn

    def _set_stars(self):
        stars = 0
        result = self.data.find("div", attrs={"class": "star mb-5"})
        if result is not None:
            stars = result["data-current"]
            self.stars = stars

    def _set_title(self):
        result = self.data.find("h1", attrs={"class": "rm_title"})
        if result is not None:
            title = result.text
            self.title = title.strip()
        else:
            self.title = "UNKNOWN"


rooms = []


def readCities() -> Any:
    with open("mizboon_city.json", "r") as f:
        jsonFile = f.read()
        f.close()
    jsonFile = json.loads(jsonFile)
    cities = jsonFile["data"]
    return cities


CITIES = readCities()


def createPath(city) -> str:
    path = ""
    for c in CITIES:
        if c["name"] == city:
            path = f"s?destination={c['id']}"

    return path


def search(city):
    # url = "https://mizboon.com/" + createPath(city)
    # response = requests.get(url).content.decode("utf-8")
    # dest = bs(response, "html5lib").find(
    #     "a", attrs={"class": "px-3 py-2 text-muted text-decoration-none d-block result"}
    # )
    # dest = dest["href"]

    canLoadMore = True
    link = "https://mizboon.com/" + createPath(city)
    while canLoadMore:
        response = requests.get(link).content.decode("utf-8")
        more_btn = bs(response, "html5lib").find(
            "a",
            attrs={
                "class": "more-result h6 my-4 text-center lh-5 rental-box border border-secondary rounded text-secondary px-3 py-1"
            },
        )
        if more_btn is not None:
            link = str(more_btn["href"])
        else:
            canLoadMore = False

    response = requests.get(link).content.decode("utf-8")
    results = bs(response, "html5lib").find("div", attrs={"class": "row search-result"})

    for r in results.find_all(
        "div",
        attrs={
            "class": "col-lg-3 col-md-6 col-12 mb-md-4 mb-5 col-lg-4 col-md-6 col-xs-12 rental-box room-link"
        },
    ):
        if len(rooms) < 10:
            link = r.find("a", attrs={"class": "room-link rental-box"})["href"]
            title = r.find("div", attrs={"class": "h6 text-dark m-0 room-title"}).text
            price = 0
            for prices in r.find_all("span", attrs={"class": "text-muted"}):
                if prices.has_attr("itemprop") and prices["itemprop"] == "price":
                    price = prices["content"]

            rooms.append(Mizboon(link, price, title, city))


# BASE_URL = "https://mizboon.com/s?"
# QUERY = "destination=45&checkin=&checkout=&adults=1&children=0&room_count=0&single_bed_count=0&double_bed_count=0&types%5B%5D=&localities%5B%5D=&facilities%5B%5D=&sort="
