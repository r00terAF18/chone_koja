from typing import Any
import requests
import json
from bs4 import BeautifulSoup as bs


class Jajiga:
    def __init__(self, id, city):
        self.id = id
        self.city = city
        self.BASE_URL = "https://www.jajiga.com/"

    def __str__(self) -> str:
        return f"Room {self.title} at {self.link}"

    def __dict__(self) -> dict:
        return {
            "UID": self.id,
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
        section = self.data.find_all("div", attrs={"class": "rm_section"})[4]
        if section is not None:
            details = section.find_all("div", attrs={"class": "rm_txt"})
            self.std_space = details[0].text.strip()
            self.max_space = details[1].text.strip()
            self.shower_count = details[2].text.strip()
            self.bathroom_count = details[3].text.strip()
            self.room_space = details[4].text.strip()
        else:
            self.std_space = "UNKNOWN"
            self.max_space = "UNKNOWN"
            self.shower_count = "UNKNOWN"
            self.bathroom_count = "UNKNOWN"
            self.room_space = "UNKNOWN"

    def setup(self) -> None:
        self._set_link()
        self._setup_data()
        self._set_ppn()
        self._set_stars()
        self._set_title()
        self._set_image()
        self.get_details()

    def _set_link(self) -> None:
        self.link = self.BASE_URL + f"room/{self.id}"

    def _setup_data(self) -> None:
        response = requests.get(self.link).content.decode("utf-8")
        self.data = bs(response, "html5lib")

    def _set_image(self) -> None:
        result = self.data.find_all("a")
        for a in result:
            if a.has_attr("data-caption"):
                self.image = a["href"]
                break
            else:
                self.image = "UNKNOWN"

    def _set_ppn(self) -> None:
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

    def _set_stars(self) -> None:
        stars = 0
        result = self.data.find("span", attrs={"class": "rate_num"})
        if result is not None:
            stars = result.text
            self.stars = stars
        else:
            self.stars = stars

    def _set_title(self) -> None:
        result = self.data.find("h1", attrs={"class": "rm_title"})
        if result is not None:
            title = result.text
            self.title = title.strip()
        else:
            self.title = "UNKNOWN"


rooms = []


def readStates() -> Any:
    with open("jaiga_city.json", "r") as f:
        jsonFile = f.read()
        f.close()
    jsonFile = json.loads(jsonFile)
    cities = jsonFile["cities"]
    return cities


CITIES = readStates()


def createPath(city) -> str:
    path = ""
    for c in CITIES:
        if c["name"] == city:
            path = f"rooms?active=true&city_with_child={c['id']}&state={c['state_id']}"

    return path


def search(city):
    url = "https://www.jajiga.com/api/v1/map/" + createPath(city)
    response = requests.get(url).content.decode("utf-8")

    response = json.loads(response)["data"]

    for r in response:
        if len(rooms) < 10:
            rooms.append(Jajiga(r["properties"]["id"], city))
        pass


# QUERY = (
#     "rooms?active=true&city_with_child=186&state=16?gstnum=2&minp=150000&maxp=5185000"
# )

#################
# def get_city():
#     for loc in STATES:
#         response = requests.get(BASE_URL + f"api/cities/{loc}").content.decode("utf-8")
#         cities = json.loads(response)
#         for c in cities:
#             CITIES.append(str(c).replace("\'", "\""))

#     # fjs = ''
#     # for c in CITIES:
#     #     fjs += str(c)

#     # fjs = json.loads(fjs)

#     with open("jaiga_city.json", "a") as f:
#         for c in CITIES:
#             f.write(str(c))
#         f.close()


# get_city()
