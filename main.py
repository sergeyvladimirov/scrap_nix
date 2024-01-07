import requests
from bs4 import BeautifulSoup
import json
import os

def get_data(url):
    
    dict_characteristics = {}
    list_project_photo_hrefs_all = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    #req = requests.get(url, headers=headers)
    #with open("projects.html", "w", encoding="utf-8") as file:
    #    file.write(req.text)
    with open("projects.html", "r", encoding = "utf-8") as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")
    articles = soup.find_all(class_="pseudoH2")
    project_urls_full = {}
    for article in articles:
        project_urls = article.get("href")
        project_title = article.text
        #project_urls_full.append("https://nix.ru" + project_urls)
        #print(f'{project_title} : {project_urls_full}')
        project_urls_full[project_title] = "https://nix.ru" + project_urls
    #print(project_urls_full)
    table_char = {}
    for name, project_url_full in project_urls_full.items():
        name = name.replace('/', '_')    
        req = requests.get(project_url_full, headers=headers)
        # Открыть для записи файлов с новыми продуктами
        with open(f"data/{name}", "w", encoding="utf-8") as file:
            file.write(req.text)
        if not os.path.isdir(os.getcwd() + '\\' + 'data' + '\\' + 'Pars' + '\\' + name):
            os.mkdir(os.getcwd() + '\\' + 'data' + '\\' + 'Pars' + '\\' + name)  
        with open(f"data/{name}", "r", encoding="utf-8") as file:
            src = file.read()
            soup = BeautifulSoup(src, "lxml")
            project_data = soup.find("div", class_ = "goods_middle")
            # take in photo of product
            try:
                project_photo = (project_data.find(id = "goods_photo").get("href"))
            except:
                project_photo = "No photo"
            # all photos of product and write in file "links {name}.txt"
            list_project_photo_hrefs_all = []
            try:
                project_photo_hrefs_all = (project_data.find("span", class_ = "carousel-content").find_all("img"))
                #print(project_photo_hrefs_all[1].get("src"))
                #list_project_photo_hrefs_all = []
                for project_photo_href_all in project_photo_hrefs_all:
                    list_project_photo_hrefs_all.append(project_photo_href_all.get("src") + '\n')
                #print(list_project_photo_hrefs_all)               
                with open(f"data/Pars/{name}/links {name}.txt", "w", encoding="utf-8") as file:
                    for str_photo in list_project_photo_hrefs_all:
                        file.write(str(str_photo)) 
                    #print(project_photo_href_all)
                #print("*" * 20)           
            except:  
                with open(f"data/Pars/{name}/links {name}.txt", "a+", encoding="utf-8") as file:
                    file.write("No Photos of product")
                    #file.write((str(list_project_photo_hrefs_all)).split(','))
            try:
                #project_description = project_data.find_all("td", class_ = "e")
                project_description = project_data.find("table", id = "PriceTable")

                for i in project_description.find_all('tr'):
                    headr = []
                    for j in i:
                        title = j.text                        
                        headr.append(title)

                    if len(headr) > 1:
                        dict_characteristics[headr[1].strip()] = headr[2].strip()
                        #print(len(headr))
                    else:
                        dict_characteristics[headr[0].strip()] = None
                        #print(len(headr))
                

                    
            except:
                print("No Description of product!")
        with open(f"data/Pars/{name}/{name}.txt", "w", encoding="utf-8") as file:
            dict_characteristics["Photo"] = project_photo
            json.dump(dict_characteristics, file, indent = 4, ensure_ascii = False)

def downlod_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    req = requests.get(url, headers=headers)
    with open(f"projects.html", "w", encoding="utf-8") as file:
        file.write(req.text)          

#downlod_html("https://www.nix.ru/lib/extra_product_news.php?offset=1&quantity=20")            



get_data("https://www.nix.ru/")

