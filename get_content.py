import requests
from bs4 import BeautifulSoup
import re


def get_content(url):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.article
    return content


be_url = 'https://wol.jw.org/de/wol/lv/r10/lp-x/0/21055'

def get_point_title_and_url(point):
    r = requests.get(be_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    title_el = soup.find(name="span", class_="title", text=re.compile(r"^\s*{} ".format(point.strip())))

    return title_el.string, "http://wol.jw.org" + title_el.parent.parent['href']


song_url = 'https://wol.jw.org/de/wol/lv/r10/lp-x/0/21056'
new_song_url = 'https://wol.jw.org/de/wol/lv/r10/lp-x/0/21057'

def get_song_title(number):
    number = int(number)

    url = song_url if number < 136 else new_song_url

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    title_el = soup.find(name="span", class_="title", text=re.compile(r"^\s*{} ".format(number)))

    r = requests.get('https://wol.jw.org' + title_el.parent.parent['href'])
    soup = BeautifulSoup(r.text, 'html.parser')

    title = "{} {} {}".format(
        number,
        soup.find(name="h1").string,
        ''.join(soup.find(class_="themeScrp").stripped_strings)
    )

    return title
