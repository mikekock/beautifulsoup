from bs4 import BeautifulSoup
import requests

base_url = 'https://blog.smokinserver.com'
index_url = base_url

response = requests.get(index_url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

posts = []
post_rows = soup.find('h2', attrs={'class': 'post-title'}).find_all('a', href=True)
for post in post_rows:
    url = post.get('href')
    title = post.get_text()
    posts.append({'url': base_url + url, 'title': title})

for post in posts:
    print(f"Scraping {post['title']}")
    response = requests.get(post['url'])
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find('article', attrs={'class': 'post'}).get_text()
