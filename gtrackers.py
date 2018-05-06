print("The links in given website")
list1 = []
from bs4 import BeautifulSoup
from urllib.request import Request,urlopen
import re
req = Request("http://svecw.edu.in")
html_page = urlopen(req)
soup = BeautifulSoup(html_page,"lxml")
links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))
for l in links:
    list1.append(l)
    print(l)
link = input("enter a link:")
l = len(list1)
count = l
k = 0
for i in range(0,l):
    if link == list1[i]:
        k = 1
        break
if k == 0:
    list1.append(link)
    count = count + 1
    print("new link has been added")
else:
    print("link already exists")
print("total number of links = ",count)
for i in list1:
    print(i)


