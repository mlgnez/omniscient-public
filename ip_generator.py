from random import randint
import requests


def generate_ip():
    string = '.'.join(
        str(randint(0, 255)) for _ in range(4)
    )
    string += ":25565"
    return string

def getLocationOfIp(ip):
    r = requests.get(f'https://ipapi.co/{ip}/json/').json()
    if not str(r).__contains__("error"):
        return r
    else:
        return {"city" : "RATE", "country_name": "LIMITED"}