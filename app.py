from flask import Flask, render_template, request
import get_content
import url_renderer
import extract_content
import datetime
import extract_form

content = get_content.get_content(url_renderer.get_current_url())

app = Flask(__name__)


@app.route('/')
def presidency():
    start_time = datetime.datetime(2000, 1, 1, 19)

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
