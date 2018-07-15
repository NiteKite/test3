from bs4 import BeautifulSoup
import requests


def scrape_followers(h):

    start_url = f'https://twitter.com/{h}'

    response = requests.get(start_url).content
    soup = BeautifulSoup(response, 'lxml')

    try:
        name = soup.find('h1', class_='ProfileHeaderCard-name').a.text
        followers = soup.find('a', attrs={'data-nav': 'followers'}).find('span', class_='ProfileNav-value')['data-count']

        return {'Name': name, 'Handle': f'@{h}', 'Followers': int(followers)}

    except AttributeError:

        return None


twitter_handle = input('\nEnter Twitter handle (excluding "@"): ')

print(scrape_followers(twitter_handle))