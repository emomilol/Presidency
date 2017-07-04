import requests
from bs4 import BeautifulSoup
import re


url1 = 'https://www.jw.org/de/publikationen/jw-arbeitsheft/april-2017-mwb/rogramm-fuer-10-16apr/'
url2 = 'https://www.jw.org/en/publications/jw-meeting-workbook/april-2017-mwb/meeting-schedule-apr17-23/'
url3 = 'https://www.jw.org/es/publicaciones/guia-actividades-reunion-testigos-jehova/abril-2017-mwb/programa-reunion-10-16abr/'
url4 = 'https://www.jw.org/de/publikationen/jw-arbeitsheft/april-2017-mwb/programm-fuer-3-9apr/'


def get_content(url):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.article
    return content


be_url = 'https://wol.jw.org/de/wol/lv/r10/lp-x/0/21033'

def get_point_title_and_url(point):
    r = requests.get(be_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    title_el = soup.find(name="span", class_="title", text=re.compile(r"^\s*{} ".format(point.strip())))

    return title_el.string, "http://wol.jw.org" + title_el.parent.parent['href']


song_url = 'https://wol.jw.org/de/wol/lv/r10/lp-x/0/21034'
new_song_url = 'https://wol.jw.org/de/wol/lv/r10/lp-x/0/21035'

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
