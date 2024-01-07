import requests
import json
from bs4 import BeautifulSoup


def get_page():
    url = "https://www.rzd.ru/"



    headers = {
        "Accept" : "*/*",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/120.0.0.0 Safari/537.36"
    }

    req = requests.get(url, headers=headers)
    src = req.text

    with open("index.html", "w", encoding="utf-8") as file:        
        file.write(src)


def third_block__links_json():
    with open("index.html", encoding="utf-8") as file:
        src = file.read()


    soup = BeautifulSoup(src, "lxml")

    all_links_dict = {}
    third_block__links = soup.find_all(class_ = "third-block__links")
    for item in third_block__links:

        z = [x for x in item.find_all('li')]
        for i in range(len(z)-1):
            
            all_links_dict[z[i].a.text] = z[i].a.get('href')
    
    with open ("data/all_links_dict.json", "w", encoding="utf-8") as file:
        json.dump(all_links_dict, file, indent = 4, ensure_ascii = False)


third_block__links_json()