import os,glob,time
import requests
from bs4 import BeautifulSoup

start_time = time.time()

urls = 'https://fappeningbook.com/'
grab = requests.get(urls)
soup = BeautifulSoup(grab.text, 'html.parser')
f = open('test1.txt' , 'w')

for link in soup.find_all("a"):
    data = link.get('href')
    f.write(data)
    f.write("\n")
f.close()

print("--- %s seconds ---" % (time.time() - start_time))