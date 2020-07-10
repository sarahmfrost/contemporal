import pandas as pd

import urllib
import requests
import shutil
from bs4 import BeautifulSoup

import time
import os
from random import randint 

titles = []
images = []

r = urllib.request.urlopen('https://americanindian.si.edu/explore/collections').read()
soup = BeautifulSoup(r)

for i in soup.find_all('div', {'class': "webmedia"}):
	titles.append(i.p.text) 

print(titles)

