import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/jobs?'
params = {
    'q' : 'Python Developer',
    'l' : 'New York State'
}

headers = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
res = requests.get(url, params=params, headers=headers)
print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())