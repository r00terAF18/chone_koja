from threading import Thread
import json
from time import sleep
from sender import send_to_api

# from Jajiga import search as jas
from Jajiga import rooms as jagrooms

from Mihmansho import search as mis
from Mihmansho import rooms as mihrooms

# from Otaghak import search as ots
# from Otaghak import rooms as othrooms

# from Mizboon import search as miz
# from Mizboon import rooms as mizrooms

# CITIES = []

# with open("jaiga_city.json", "r") as f:
#     data = json.load(f)["cities"]
#     for city in data:
#         CITIES.append(city["name"])
#     f.close()


def add_data(city):
    ###### ADD ROOMS ######
    threads = []

    # threads.append(Thread(target=jas, args=(city,)))
    threads.append(Thread(target=mis, args=(city,)))
    # threads.append(Thread(target=ots, args=(city,)))
    # threads.append(Thread(target=miz, args=(city,)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    ###### INIT ROOM DATA ######

    def init_rooms(list):
        for room in list:
            room.setup()
            print(room.__dict__())

    threads = []

    # threads.append(Thread(target=init_rooms, args=(jagrooms,)))
    threads.append(Thread(target=init_rooms, args=(mihrooms,)))
    # threads.append(Thread(target=init_rooms, args=(mizrooms,)))
    # threads.append(Thread(target=init_rooms, args=(othrooms,)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    ###### SEND ROOMS ######

    # def send(list):
    #     for room in list:
    #         data = room.__dict__()
    #         send_to_api(data)

    # threads = []

    # threads.append(Thread(target=send, args=(jagrooms,)))
    # threads.append(Thread(target=send, args=(mihrooms,)))
    # threads.append(Thread(target=send, args=(mizrooms,)))
    # threads.append(Thread(target=send, args=(othrooms,)))

    # for t in threads:
    #     t.start()

    # for t in threads:
    #     t.join()


try:
    CITIES = ["اهواز", "شیراز", "مشهد"]
    for city in CITIES:
        print(f"Collecting data for {city}")
        add_data(city)
        sleep(25)
        print("\n\n")
except:
    print('meh!')
    pass
