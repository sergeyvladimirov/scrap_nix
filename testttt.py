import requests
from bs4 import BeautifulSoup
import json

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

req = requests.get("https://static.nix.ru/images/%ED%E8%EA%F1-as6000-s635fpai-7615222254.jpg?good_id=761522&width=500&height=500&view_id=2254", headers=headers)


r