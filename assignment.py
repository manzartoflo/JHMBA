#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:48:59 2019

@author: manzars
"""
import requests
from bs4 import BeautifulSoup

url = "http://www.jhmba.com.my/index.php?ws=pages&pages_id=3346"

req = requests.get(url)
soup = BeautifulSoup(req.text, 'lxml')
tds = soup.findAll('table')[0].findAll('td')[1::3]

email = []
for td in tds:
    try:
        if('@' in td.text.replace('\n', '').replace('\xa0', '')):
            email.append(td.text.replace('\n', '').replace('\xa0', ''))
    except:
        pass
    

num = []
for td in tds:
    try:
        if(not any(x.isalpha() for x in td.text.replace('\n', '').replace('\xa0', '').replace('\t', '').replace('\r', ''))):
            num.append(td.text.replace('\n', '').replace('\xa0', '').replace('\t', '').replace('\r', ''))
    except:
        pass
    
web = []
for td in tds:
    try:
        if('www' in td.text.replace('\n', '').replace('\xa0', '')):
            web.append(td.text.replace('\n', '').replace('\xa0', ''))
    except:
        pass
    
name = []
for td in tds:
    try:
        
        if(td.text.replace('\n', '').replace('\xa0', '') == td.text.replace('\n', '').replace('\xa0', '').upper()):
            name.append(td.text.replace('\n', '').replace('\xa0', ''))
        
    except:
        pass
count = 0
for x in name:
    if('\r' in x):
        name.pop(count)
    count += 1
    
count = 0
for x in name:
    if('\r' in x):
        name.pop(count)
    count += 1

count = 0
for x in name:
    if(not any(c.isalpha() for c in x)):
        name.pop(count)
    count += 1

count = 0
for x in name:
    if(not any(c.isalpha() for c in x)):
        name.pop(count)
    count += 1
count = 0
for x in num:
    if(x == ''):
        num.pop(count)
    count += 1

tel = num[0::2]
fax = num[1::2]

header = "Company Name, Telephone, Fax, Email\n"
file = open('assignment.csv', 'w')
file.write(header)

for i in range(201):
    file.write(name[i].replace(',', '') + ', ' + tel[i].replace(',', ' | ') + ', ' + fax[i].replace(',', ' | ') + ', ' + email[i].replace(',', ' | ') + '\n')
file.close()