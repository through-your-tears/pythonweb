import requests
import re
from bs4 import BeautifulSoup


s = [' ', ',', '.', '! ', '?','"', ';', ':', '[', ']', '(', ')', '\n', '\r', '\t']

r = requests.get('https://www.simbirsoft.com/')
soup = BeautifulSoup(r.text, 'html.parser')
res = soup.find('body')
res = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', str(res))
res = re.sub(r'(\<(/?[^>]+)>)', '', str(res))

a = res.split()
d = {}
for x in a:
    if x[0] in s:
        x = x[1:]
    elif x[-1] in s:
        x = x[:-1]
    if d.get(x):
        d[x] += 1
    else:
        d[x] = 1
for x in d.keys():
    print(f'{x} - {d[x]}')
