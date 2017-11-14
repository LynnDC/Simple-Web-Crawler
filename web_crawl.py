import requests
import bs4

import time
import urllib

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"

"""define helper function to request a url and parse it to find the 1st link within it"""


def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    article_link = None
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            first_relative_link = element.find("a", recursive=False).get('href')
            break
    if not article_link:
        return first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)
    return first_link

"""define a helper function to set conditions on our main function later so we
don't end up with infinate loops"""


def continue_crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:
        print('we\'ve found thet target article!')
        return False
    elif len(search_history) > max_steps:
        print('The search has gone too long')
        return False
    elif search_history[-1] in search_history[:-1]:
        print('we\'ve already seen this article')
        return False
    else:
        return True


article_chain = [start_url]


while continue_crawl(article_chain, target_url):
    print(article_chain[-1])
    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print("This article has no links.")
        break
    article_chain.append(first_link)
    time.sleep(2)
