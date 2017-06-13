from flask import Flask, render_template, request
import get_content
import url_renderer
import extract_content
import datetime
import extract_form

url1 = 'https://www.jw.org/de/publikationen/jw-arbeitsheft/april-2017-mwb/rogramm-fuer-10-16apr/'
url2 = 'https://www.jw.org/en/publications/jw-meeting-workbook/april-2017-mwb/meeting-schedule-apr17-23/'
url3 = 'https://www.jw.org/es/publicaciones/guia-actividades-reunion-testigos-jehova/abril-2017-mwb/programa-reunion-10-16abr/'
url4 = 'https://www.jw.org/de/publikationen/jw-arbeitsheft/mai-2017-mwb/programm-fuer-15-21mai/'
content = get_content.get_content(url4)

app = Flask(__name__)


@app.route('/')
def presidency():
    start_time = datetime.datetime(1, 1, 1, 19)

    header = extract_content.header(content)
    sections = [extract_content.section1(content), extract_content.section2(content), extract_content.section3(content),
                extract_content.section4(content)]

    for section in sections:
        for item in section.items:
            item.time = start_time.time()
            start_time += datetime.timedelta(minutes=item.duration)

    return render_template("sections.html", sections=sections, header=header, start_time=start_time)


@app.route('/', methods=['POST'])
def form_post():
    tree, section_title = extract_form.create_tree(request.form)
    #print tree, section_title
    header = extract_content.header(content)
    sections = [extract_form.section1(tree, section_title), extract_form.section2(tree, section_title),
                extract_form.section3(tree, section_title), extract_form.section4(tree, section_title)]

    return render_template("finished/sections.html", sections=sections, header=header)


if __name__ == '__main__':
    app.run(debug=True)
