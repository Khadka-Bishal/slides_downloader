import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

#base URL
base_url = input("Enter url here: ")

#send a GET request and do not veritfy HTTPS request
response = requests.get(base_url, verify=False)

#parse the content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

#find all links on the page
links = soup.select('a[href$=".pdf"]')

#get the current working directory
current_directory = os.getcwd()

for link in links:
    filename = os.path.join(current_directory, link['href'].split('/')[-1])
    with open(filename, 'wb') as out_file:
        response = requests.get(urljoin(base_url, link['href']), verify=False)
        out_file.write(response.content)