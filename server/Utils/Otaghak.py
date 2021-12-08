from typing import Any
import requests
import json
from bs4 import BeautifulSoup as bs

QUERY = "https://core.otaghak.com/api/v1/Search/GetSearchResult?input="
QUERY_ROOMS = "https://www.otaghak.com/city/cityCode?sortingtype=OtaghakSuggestions&aroundlocations=true&page=1"


class Otaghak:
    def __init__(self, data, city):
        self.data = data
        self.city = city
        self.BASE_URL = "https://otaghak.com"

    def __str__(self) -> str:
        return f"Room {self.title} at {self.link}"

    def __dict__(self) -> dict:
        return {
            "UID": self.UID,
            "title": self.title,
            "link_to_site": self.link,
            "price_per_night": self.price_per_night,
            "rating": self.stars,
            "state": "",
            "city": self.city,
        }

    def setup(self) -> None:
        # self._setup_data()
        self._set_link()
        self._set_ppn()
        self._set_stars()
        self._set_title()

    def _set_link(self):
        link = self.data.find("a", attrs={"class": "room-box-container"})["href"]
        self.link = self.BASE_URL + f"{link}"
        self.UID = self.link.split("/")[-1]

    def _setup_data(self):
        response = requests.get(self.link).content.decode("utf-8")
        self.data = bs(response, "html5lib")

    def _set_ppn(self):
        ppn = 0
        li = self.data.find("span", attrs={"style": "font-size:16px;color:#303030;"})
        if li is not None:
            ppn = li.text.strip()
        self.price_per_night = ppn

    def _set_stars(self):
        response = requests.get(self.link).content.decode("utf-8")
        data = bs(response, "html5lib")
        stars = 0
        result = data.find("span", attrs={"class": "rating-total__span"})
        if result is not None:
            stars = result.text.strip()
            self.stars = stars
        else:
            self.stars = stars

    def _set_title(self):
        result = self.data.find("div", attrs={"class": "room-title"})
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
    url = QUERY + city
    response = requests.get(url).content.decode("utf-8")

    response = json.loads(response)
    cityCode = response[0]["cityCode"]
    url = f"https://www.otaghak.com/city/{cityCode}?sortingtype=OtaghakSuggestions&aroundlocations=true&page=1"

    response = requests.get(url).content.decode("utf-8")

    results = bs(response, "html5lib").find_all("div", attrs={"class": "all-container"})

    for r in results:
        if len(rooms) < 10:
            rooms.append(Otaghak(r, city))

    canLoadMore = True
    # link = "https://mizboon.com/" + createPath(city)
    # while canLoadMore:
    #     response = requests.get(link).content.decode("utf-8")
    #     more_btn = bs(response, "html5lib").find(
    #         "a",
    #         attrs={
    #             "class": "more-result h6 my-4 text-center lh-5 rental-box border border-secondary rounded text-secondary px-3 py-1"
    #         },
    #     )
    #     if more_btn is not None:
    #         link = str(more_btn["href"])
    #     else:
    #         canLoadMore = False

    # response = requests.get(link).content.decode("utf-8")
    # results = bs(response, "html5lib").find("div", attrs={"class": "row search-result"})

    # for r in results.find_all(
    #     "div",
    #     attrs={
    #         "class": "col-lg-3 col-md-6 col-12 mb-md-4 mb-5 col-lg-4 col-md-6 col-xs-12 rental-box room-link"
    #     },
    # ):
    #     link = r.find("a", attrs={"class": "room-link rental-box"})["href"]
    #     title = r.find("div", attrs={"class": "h6 text-dark m-0 room-title"}).text
    #     price = 0
    #     for prices in r.find_all("span", attrs={"class": "text-muted"}):
    #         if prices.has_attr("itemprop") and prices["itemprop"] == "price":
    #             price = prices["content"]

    #     rooms.append(Otaghak(link, price, title))
