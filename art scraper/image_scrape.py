# have to install these on your computer
from bs4 import BeautifulSoup
import requests as rq

import os

r2 = rq.get("https://collections.si.edu/search/gallery.htm?og=national-museum-of-the-american-indian")
soup2 = BeautifulSoup(r2.text, "html.parser")

links = []

x = soup2.select('img')

for img in x:
    links.append(img)

# for l in links:
#      print(l.get('src'))

# i = 1

for index, img in enumerate(links):
    img_link = img.get('src')
    title = img.get('alt')
    if "/" in title:
        title = title.replace("/", "")
    print(img_link)
    if img_link[:1]=="h":
        img_data = rq.get(img_link).content
        with open("art_photos/" + title + '.jpg', 'wb+') as f:
            f.write(img_data)
    # i += 1

links2 = []
for link in soup2.find_all('a'):
    if link.has_attr('href'):
        links2.append(link.attrs['href'])

links2 = [lin for lin in links2 if 'results.htm?' in lin]

links3 = []
for lin in links2:
    lin = lin[:0] + "https://collections.si.edu/search/" + lin[0:]
    links3.append(lin)

print(links3)
