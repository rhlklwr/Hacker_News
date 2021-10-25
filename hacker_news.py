import requests
from bs4 import BeautifulSoup
import pprint

page = input('Enter number of page you want to get the news: ')

url = f"https://news.ycombinator.com/news?p={page}"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def hacker_news(links, subtext):
    hn = []
    for index ,item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(hacker_news(links, subtext))