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
tomorrow = datetime.today() + timedelta(1)
tomorrow = tomorrow.strftime('%Y-%b-%d')

#pp = pprint.PrettyPrinter(indent=4).pprint

chrome_options = Options()
#chrome_options.add_extension("proxy.zip")
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path='/home/kevin/scripts/selenium/chromedriver', chrome_options=chrome_options)

url = 'https://xxxxxxxxxxxxxxxxxxxxxxxx'
url2 = 'xxxxxxxxxxxxxxxxxx'
url3 = 'xxxxxxxxxxxxxxxxxx'

driver.get(url)
driver.get(url3)
page = driver.page_source
soup = bs4(page, 'html.parser')

regex2 = re.findall(r"(.*href)*=\"(.*)(mkv).*(.mkv\")(.*)(\d{4}-[a-zA-Z]{3}-\d{2} \d{2}:\d{2})", page)

tables = soup.findChildren('table')
my_table = tables[0]
rows = my_table.findChildren(['tr'])
dates = []

for row in rows:
	cells = row.findChildren('td')
	for cell in cells:
		value = cell.string
		dates.append(value)

dldates = [k for k in dates if (str(yesterday)) in k]
dldates1 = [k for k in dates if (str(today)) in k]
dldates2 = [k for k in dates if str(tomorrow) in k]
dldates3 = (dldates + dldates1 + dldates2)

x2 = []

for items in regex2:
	for datez in dldates3:
		if str(items[5]) == datez:
			x2.append(str(items[1]) + 'mkv')

pcfiles = os.listdir("/home/kevin/Downloads")
pcfiles = sorted(pcfiles)

downloadmkv = list(set(x2) - set(pcfiles))
downloadmkv = sorted(downloadmkv)

for itemz in downloadmkv:
	itemz = ('https://xxxxxxxx/Extracted/' + itemz)
	driver.get(itemz)


def download_wait(path_to_downloads):
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < 20:
        time.sleep(1)
        dl_wait = False
        for fname in os.listdir(path_to_downloads):
            if fname.endswith('.crdownload'):
                dl_wait = True
        seconds += 1
    return seconds
	
driver.close()

