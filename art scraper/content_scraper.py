# have to install these on your computer
from bs4 import BeautifulSoup
import requests as rq

import os
import re
import csv 

# #testing to go into each art piece for 1 category
# content = []
# c1 = rq.get("https://collections.si.edu/search/results.htm?q=%22Adornment%2FJewelry%22&fq=data_source%3A%22National+Museum+of+the+American+Indian%22&fq=online_media_type%3A%22Images%22&view=grid")
# contentsoup = BeautifulSoup(c1.text, "html.parser")
# clink = []
# for link in contentsoup.find_all('a'):
#     if link.has_attr('href'):
#         clink.append(link.attrs['href'])

# clink = [lin for lin in clink if 'results.htm?' in lin]

# clink1 = []

# for lin in clink:
#     lin = lin[:0] + "https://collections.si.edu/search/" + lin[0:]
#     clink1.append(lin)

# for i in clink1:
#     c2 = rq.get(i)
#     contentsoup1 = BeautifulSoup(c2.text, "html.parser")
#     y = contentsoup1.findAll("div",{"class":"meta"})
#     for detail in y:
#         content.append(detail)
with open('content.csv', mode='w') as content:
    content = csv.writer(content, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    content.writerow(["name", "culture", "media", "otype", "place", "history"])

c1 = rq.get("https://collections.si.edu/search/detail/edanmdm:NMAI_248665?hlterm=%26quot%3BPainting%2FDrawing%2FPrint%26quot%3B")
contentsoup = BeautifulSoup(c1.text, "html.parser")

name = contentsoup.findAll("dd",{"class":"physicalDescription-first"})
name = name[0].getText()
name = re.sub(' +',' ',name)

culture = contentsoup.findAll("dd",{"class":"name-first"})
culture = culture[0].getText()
culture = re.sub(' +',' ',culture)
print('<p class="content"> CULTURE/PEOPLE:' + culture.replace("Search this", "") + "</p>")
# f.write('<p class="content"> CULTURE/PEOPLE:' + culture + '</p>' )

media = contentsoup.findAll("dd",{"class":"physicalDescription"})
media = media[1].getText()
media = re.sub(' +',' ',media)
print('<p class="content"> MEDIA/MATERIALS:' + media + '</p>')

otype = contentsoup.findAll("dd",{"class":"objectType-first"})
otype = otype[0].getText()
otype = re.sub(' +',' ',otype)
print('<p class="content"> OBJECT TYPE:' + otype + '</p>')

place = contentsoup.findAll("dd",{"class":"place-first"})
place = place[0].getText()
place = re.sub(' +',' ',place)
print('<p class="content"> PLACE:' + place + '</p>')

history = contentsoup.findAll("dd",{"class":"notes-first"})
history = history[0].getText()
history = re.sub(' +',' ',history)
print('<p class="content"> COLLECTION HISTORY::' + history + '</p>')

with open('content.csv', mode='w') as content:
    content = csv.writer(content, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    content.writerow([name, culture, media, otype, place, history])

