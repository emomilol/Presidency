import requests
from bs4 import BeautifulSoup



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




