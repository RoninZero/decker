#!/usr/bin/env python3
import os
import requests
from bs4 import BeautifulSoup


url = 'http://netrunnerdb.com/login'

body = {'username':'NotMyUsername','password':'NotMyPassword'}

s = requests.Session()

loginPage = s.get(url)

soup = BeautifulSoup(loginPage.text, 'html.parser')

hiddenInputs = soup.findAll(name = 'input', type = 'hidden')

for hidden in hiddenInputs:
    print('hidden', hidden)
    name = hidden['name']
    value = hidden['value']
    body[name] = value

print('name:', name)
print('value:', value)
print('body[name]:', body[name])

# r = s.post(soup.form['action'], data=body)
#r = s.post(url, data = body)
