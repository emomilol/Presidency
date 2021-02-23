import models
from get_content import get_point_title_and_url, get_song_title
import re

def set_song_subtitle(song):
    m = re.match(r"[^\d]*(\d+)", song.title)
    song.subtitle = get_song_title(m.group(1))


def create_tree(form):
    tree = [[], [], [], []]
    section_titles = ['', '', '', '']

    for key, value in form.items():
        split = key.split('.')

        if len(split) == 3:
            field, section, item = split
            section, item = int(section), int(item)

            while len(tree[section]) <= item:
                tree[section].append({})

            tree[section][item][field] = value

        else:
            title, section = split
            section = int(section)
            section_titles[section] = value

    return tree, section_titles


def section1(tree, titles):
    item0 = tree[0][0]
    song = models.Assignment(item0['title'], 5, item0['assignee'])
    song.time = item0['time']

    set_song_subtitle(song)

    item1 = tree[0][1]
    comments = models.ProgramItem(item1['title'], 1)
    comments.time = item1['time']
    comments.comments = item1['comments']

    items = [song, comments]

    section = models.Section(titles[0], items)

    return section


def section2(tree, titles):
    item0 = tree[1][0]
    treasures = models.Assignment(item0['title'], item0['duration'], item0['assignee'])
    treasures.time = item0['time']

    item1 = tree[1][1]
    gems = models.Assignment(item1['title'], item1['duration'], item1['assignee'])
    gems.time = item1['time']

    item2 = tree[1][2]
    reading = models.StudentsAssignment(item2['title'], item2['duration'],
                                        item2['student'], None,
                                        item2['point'])
    reading.time = item2['time']

    items = [treasures, gems, reading]

    sections = models.Section(titles[1], items)

    return sections


def section3(tree, titles):
    items = []

    for index, item in enumerate(tree[2]):
        if 'student' in item:
            index = models.StudentsAssignment(item['title'], item['duration'],
                                              item['student'], item['partner'],
                                              item['point'])
            index.time = item['time']
            items.append(index)
        else:
            index = models.Assignment(item['title'], item['duration'],
                                      item['assignee'])
            index.time = item['time']

            items.append(index)

    section = models.Section(titles[2], items)

    return section


def section4(tree, titles):
    items = []

    song = models.ProgramItem(tree[3][0]['title'], tree[3][0]['duration'])
    song.time = tree[3][0]['time']

    set_song_subtitle(song)

    items.append(song)

    for index, item in enumerate(tree[3][1:-2]):
        index = models.Assignment(item['title'], item['duration'],
                                  item['assignee'])
        index.time = item['time']
        items.append(index)

    comments = models.ProgramItem(tree[3][-2]['title'], 3)
    comments.time = tree[3][-2]['time']
    items.append(comments)

    prayer = models.Assignment(tree[3][-1]['title'], 5,
                               tree[3][-1]['assignee'])
    prayer.time = tree[3][-1]['time']

    set_song_subtitle(prayer)

    items.append(prayer)

    section = models.Section(titles[3], items)

    return section
