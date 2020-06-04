# All requirement
from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import time


### Get all users from a blocklist

start = time()
account = []

max_page = 378 # Enter here the number of page there's in a list (divide len of list by account per page)

for i in range(1, int(max_page)+1):
    url = "https://blocktogether.org/show-blocks/tlHlZUnVX97LG0_MrO8qVGoewdwI5sVNf-ZCwfkr?page=" + str(i) # Change the URL by the URL of the list with the "?page=" at the end (do not put a number)
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    for link in soup.find_all('a', class_='screen-name'):
        account.append(link.get('href'))


print(f"len of account : {len(account)}")
df = pd.DataFrame({'accounts': account})
df.to_csv('accounts.csv', index=False, encoding='utf-8')
stop = time()
print("Running time : ", stop - start)