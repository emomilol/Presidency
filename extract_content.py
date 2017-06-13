from bs4 import BeautifulSoup
import get_content
import models


def header(html):
    week = html.h1.get_text()
    reading = html.h2.get_text()

    return models.Header(week, reading)


def section1(html):
    section_str = html.find(id='section1')
    items = [
        section1_part1(section_str),
        section1_part2(section_str)
    ]

    section = models.Section('', items)

    return section


def section1_part1(section):
    song = section.find(id='p3')

    opening_song = song.get_text()
    song_duration = 5

    item = models.Assignment(opening_song, song_duration)

    return item


def section1_part2(section):
    comments = section.find(id='p4')

    opening_comments = comments.get_text()
    comments_duration = 3

    item = models.ProgramItem(opening_comments, comments_duration)

    return item


def section2(html):
    section = html.find(id='section2')

    items = [
        section2_part1(section),
        section2_part2(section),
        section2_part3(section)
    ]

    section = models.Section(section2_title(section), items)

    return section


def section2_title(section):
    title = section.h2.string

    return title


def section2_part1(section):
    part1 = section.find(id='p6')

    treasures = part1.get_text()
    treasures_duration = 10
    item = models.Assignment(treasures, treasures_duration)

    return item


def section2_part2(section):
    part2 = section.find(id='p10')

    gems = part2.get_text()
    gems_duration = 8

    item = models.Assignment(gems, gems_duration)

    return item


def section2_part3(section):
    part3 = section.find(id='p15')

    reading = part3.get_text()
    reading_duration = 4

    item = models.StudentsAssignment(reading, reading_duration, partner=None)

    return item


def section3(html):
    section = html.find(id='section3')
    section = models.Section(
        section3_title(section),
        section3_items(section)
    )

    return section


def section3_title(section):
    title = section.h2.string

    return title


def section3_items(section):
    list_items = section.findAll('li')
    L = []
    if len(list_items) == 1:
        title, duration = extract_name_and_duration(list_items[0])
        return [models.Assignment(title, duration)]

    for item in list_items:
        title, duration = extract_name_and_duration(item)
        L.append(models.StudentsAssignment(title, duration + 1))

    return L


def section4(html):
    section = html.find(id='section4')
    section = models.Section(
        section4_title(section),
        section4_parts(section)
    )

    return section


def section4_title(section):
    title = section.h2.string

    return title


def section4_parts(section):
    list_items = section.findAll('li')
    items = []

    song = list_items[0]
    items.append(models.ProgramItem(song.get_text(), 3))

    for item in list_items[1:-2]:
        text, duration = extract_name_and_duration(item)
        items.append(models.Assignment(text, duration))

    end_comments = list_items[-2]
    items.append(models.ProgramItem(end_comments.get_text(), 3))

    end_song = list_items[-1]
    items.append(models.Assignment(end_song.get_text(), 5))

    return items


def extract_name_and_duration(item):
    text = unicode(item.get_text())
    if ')' in text:
        end = text.rfind(')')
        text = text[:end + 1]

    duration_str = text[text.rfind('('):]
    duration = int(filter(unicode.isdigit, duration_str))
    return text, duration
