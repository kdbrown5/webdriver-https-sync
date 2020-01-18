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
import  sys
today = datetime.today().strftime('%Y-%b-%d')
yesterday = datetime.today() - timedelta(1)
yesterday = yesterday.strftime('%Y-%b-%d')
tomorrow = datetime.today() + timedelta(1)
tomorrow = tomorrow.strftime('%Y-%b-%d')

#pp = pprint.PrettyPrinter(indent=4).pprint

chrome_options = Options()
#chrome_options.add_extension("proxy.zip")
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)

url = 'https://xxxxxx'
#url2 = 'https://xxxxxx'
url3 = 'https://xxxxxx/Extracted/'

driver.get(url)
driver.get(url3)
page = driver.page_source
soup = bs4(page, 'html.parser')

parsesoup = re.findall(r"(.*href)*=\"(.*)(mkv).*(.mkv\")(.*)(\d{4}-[a-zA-Z]{3}-\d{2} \d{2}:\d{2})", page)

tables = soup.findChildren('table')
tables1 = tables[0]
rows = tables1.findChildren(['tr'])
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

servermkv = []

for items in parsesoup:
	for datez in dldates3:
		if str(items[5]) == datez:
			servermkv.append(str(items[1]) + 'mkv')

pcdir = "/python"
pcfiles = os.listdir(pcdir)
pcfiles = sorted(pcfiles)

downloadmkv = list(set(servermkv) - set(pcfiles))
downloadmkv = sorted(downloadmkv)

for itemz in downloadmkv:
	itemz = ( url3 + itemz)
	driver.get(itemz)

waittime=0
while waittime==0:
    count=0
    li = os.listdir("/python")
    for waittime in li:
        if waittime.endswith(".crdownload"):
             count = count+1        
    if count==0:
        waittime=1
    else:
        waittime=0

time.sleep(2)
        
driver.close()
driver.quit()
sys.exit()
