# -scraping-website

## Project Overview
This is a python program that expands on [click link](https://www.py4e.com/code3/urllinks.py). The program will use urllib to read the HTML from the data files below, extract the href= values from the anchor tags, scan for a tag that is in a particular position from the top and follow that link, repeat the process a number of times, and report the last name you find.

```Python3
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL:')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Elvi.html'
counts = int(input('Enter count:'))
position = int(input('Enter position:'))

for i in range(counts):
    html = urllib.request.urlopen(url).read()
    soup  = BeautifulSoup(html,'html.parser')
    
    tag = soup('a')
    url = tag[position - 1].get('href', None)
    print("Retrieving:",url)

lastname = url.split('_')[2].split(".")[0]
print(lastname)
```
