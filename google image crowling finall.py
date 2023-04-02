import os
import requests
from bs4 import BeautifulSoup

query = "이명박"

download_path = os.path.join(os.path.expanduser("~"), "Users\liu39\OneDrive\Desktop", query)

url = f"https://www.google.com/search?q={query}&tbm=isch"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
image_elements = soup.select("img.rg_i")

image_urls = []
for i, image_element in enumerate(image_elements):
    if "src" in image_element.attrs:
        image_urls.append(image_element["src"])
    elif "data-src" in image_element.attrs:
        image_urls.append(image_element["data-src"])
    elif "data-iurl" in image_element.attrs:
        image_urls.append(image_element["data-iurl"])

if not os.path.exists(download_path):
    os.makedirs(download_path)
for i, image_url in enumerate(image_urls):
    image_name = f"{query}_{i}.jpg"
    download_path_full = os.path.join(download_path, image_name)
    try:
        response = requests.get(image_url, headers=headers)
        with open(download_path_full, "wb") as f:
            f.write(response.content)
        print(f"{image_name} Download completed")
    except:
        print(f"{image_name} Download failed")
