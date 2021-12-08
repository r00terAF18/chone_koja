from requests import post

URL = "http://127.0.0.1:8000/api/v1/create/"

def send_to_api(data):
    post(URL, data=data)

