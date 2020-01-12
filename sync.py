import requests
import pprint
import re
from string import ascii_letters
from bs4 import BeautifulSoup as bs4
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import urllib.request
import os
import datetime
from os import listdir
from os.path import isfile, join
from datetime import datetime, timedelta
today = datetime.today().strftime('%Y-%b-%d')
yesterday = datetime.today() - timedelta(1)
yesterday = yesterday.strftime('%Y-%b-%d')

pp = pprint.PrettyPrinter(indent=4).pprint

chrome_options = Options()
#chrome_options.add_extension("proxy.zip")
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)

url = 'https://site.com/dl'
url2 = 'https://site.com/dl2'
url3 = 'https://site.com/dl3'
driver.get(url)
driver.get(url3)
page = driver.page_source
soup = bs4(page, 'html.parser')

tables = soup.findChildren('table')
my_table = tables[0]
rows = my_table.findChildren(['tr'])
dates = []
for row in rows:
	cells = row.findChildren('td')
	for cell in cells:
		value = cell.string
		dates.append(value)

newdownload = []
for row in rows:
	cells = row.findChildren('td')
	for cell in cells:
		if '2020-Jan-04' in str(cells):
			newdownload.append(cell)


dldates = [k for k in dates if '2020' in k]

servermkv = [a['href'] for a in soup.find_all('a', href=True)]
servermkv = sorted(servermkv)
del servermkv[0:8]


with open('files.txt', 'w') as filehandle:
    for listitem in servermkv:
        filehandle.write('%s\n' % listitem)

pcfiles = os.listdir("/python")
pcfiles = sorted(pcfiles)

downloadmkv = list(set(servermkv) - set(pcfiles))
downloadmkv = sorted(downloadmkv)

with open('pcfiles.txt', 'w') as filehandle:
    for listitem in pcfiles:
        filehandle.write('%s\n' % listitem)

with open('downloadmkv.txt', 'w') as filehandle:
    for listitem in downloadmkv:
        filehandle.write('%s\n' % listitem)


res = [ele for ele in dldates if(ele in rows)] 
#print(soup)
