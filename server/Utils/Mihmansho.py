from typing import Any
import requests
import json
from bs4 import BeautifulSoup as bs


class Mihman:
    def __init__(self, data, city, state):
        self.data = data
        self.city = city
        self.state = state
        self.BASE_URL = "https://www.mihmansho.com/"

    def __str__(self) -> str:
        return f"Room {self.title} at {self.link}"

    def __dict__(self) -> dict:
        return {
            "UID": self.UID,
            "image_link": self.image,
            "title": self.title,
            "link_to_site": self.link,
            "price_per_night": self.price_per_night,
            "rating": self.stars,
            "state": "",
            "city": self.city,
            "std_space": self.std_space,
            "max_space": self.max_space,
            "shower_count": self.shower_count,
            "bathroom_count": self.bathroom_count,
            "room_space": self.room_space,
        }

    def get_details(self) -> None:
        section = self.data.find_all("div", attrs={"class": "col-md-4 col-sm-6"})
        if section is not None:
            self.std_space = section[4].text.strip()
            # self.max_space = section[7].text.strip()
            # self.shower_count = "1"
            # self.bathroom_count = "1"
            # self.room_space = section[5].text.strip()
            self.max_space = "در حال حاظر موجود نیست"
            self.shower_count = "در حال حاظر موجود نیست"
            self.bathroom_count = "در حال حاظر موجود نیست"
            self.room_space = "در حال حاظر موجود نیست"
        else:
            self.std_space = "در حال حاظر موجود نیست"
            self.max_space = "در حال حاظر موجود نیست"
            self.shower_count = "در حال حاظر موجود نیست"
            self.bathroom_count = "در حال حاظر موجود نیست"
            self.room_space = "در حال حاظر موجود نیست"

    def setup(self) -> None:
        self._set_link()
        self._set_ppn()
        self._set_stars()
        self._set_title()
        self._set_image()
        self.get_details()

    def _set_image(self) -> None:
        self.data = bs(requests.get(self.link).content.decode("utf-8"), "html5lib")
        result = self.data.find("img", attrs={"id": "first-image"})
        if result is not None:
            self.image = result["src"]
        else:
            self.image = "UNKNOWN"

    def _set_ppn(self) -> None:
        ppn = 0
        li = self.data.find("span", attrs={"class": "per-night"})
        if li is not None:
            ppn = li.parent.text.strip().replace("تومان", "").strip()
        self.price_per_night = ppn

    def _set_stars(self) -> None:
        stars = 0
        div = self.data.find("div", attrs={"class": "five-stars-container"})
        if div is not None:
            stars = div["title"].split(" ")[1]
            self.stars = stars
        else:
            self.stars = stars

    def _set_title(self) -> None:
        if self.data.find("h2", attrs={"class": "box-title"}) is not None:
            title = self.data.find("h2", attrs={"class": "box-title"}).text
            self.title = title.strip()
        else:
            self.title = "UNKNOWN"

    def _set_link(self) -> None:
        rId = self.data["data-id"]
        self.UID = rId
        self.link = self.BASE_URL + f"room/{rId}"


rooms = []
state = ""


def readLoc() -> Any:
    with open("mihmansho_city.json", "r") as f:
        jsonFile = f.read()
        f.close()
    jsonFile = json.loads(jsonFile)
    cities = jsonFile["CitiesHome"]
    return cities


BASE_URL = "https://www.mihmansho.com/"
LOCATIONS = readLoc()


def createPath(city) -> str:
    path = ""
    for c in LOCATIONS:
        if c["CityName"] == city:
            state = c["StateName"]
            path = "property/" + c["StateLatinName"] + "/" + c["CityLatinName"]
            return path


def search(city):
    url = BASE_URL + createPath(city)
    response = requests.get(url).content.decode("utf-8")

    soup = bs(response, "html5lib")
    ul = soup.find("ul", attrs={"id": "result-list"})

    for li in ul.find_all("li"):
        if li.has_attr("data-id") and len(rooms) < 10:
            rooms.append(Mihman(li, city, state))


def _locsearch():
    with open("index.html", "r") as f:
        html = f.read()
        f.close()
    ul = bs(html, "html5lib").find("ul", attrs={"id": "result-list"})


# debug search
# _locsearch()
