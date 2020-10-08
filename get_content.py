import requests
from bs4 import BeautifulSoup
import re


def get_content(url):
    r = requests.get(url)
    r.raise_for_status()
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.article
    return content

def get_soup_from_enhanced_url(enhanced_url):
    chain = [s.strip() for s in enhanced_url.split('>')]

    url = chain[0]
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    for link_text in chain[1:]:
        link_el = soup.find(class_="title", string=link_text)
        if link_el is None:
            return None

        while link_el.name != 'a':
            link_el = link_el.parent

        url = 'https://wol.jw.org' + link_el['href']
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

    return soup


be_url = 'https://wol.jw.org/de/wol/lv/r10/lp-x/0 > Bücher > Predigtdienstschul-Buch  (be)'

def get_point_title_and_url(point):
    soup = get_soup_from_enhanced_url(be_url)
    if soup is None:
        return '', ''

    title_el = soup.find(name="span", class_="title", text=re.compile(r"^\s*{} ".format(point.strip())))
    title = title_el.string if title_el is not None else ''

    link = "http://wol.jw.org" + title_el.parent.parent['href'] if title_el is not None else ''
    return title, link


song_url = 'https://wol.jw.org/es/wol/library/r4/lp-s/biblioteca > Libros > Cantemos con gozo (sjj)'

def get_song_title(number):
    number = int(number)

    soup = get_soup_from_enhanced_url(song_url)
    print(soup)
    if soup is None:
        return ''

    title_el = soup.find(name="span", class_="title", text=re.compile(r"^\s*{} ".format(number)))

    r = requests.get('https://wol.jw.org' + title_el.parent.parent['href'])
    soup = BeautifulSoup(r.text, 'html.parser')

    title = "{} {} {}".format(
        number,
        soup.find(name="h1").string,
        ''.join(soup.find(class_="themeScrp").stripped_strings)
    )

    return title
