class Header(object):
    template = 'header.html'

    def __init__(self, week, reading):
        self.heading = week
        self.reading = reading


class ProgramItem(object):
    template = "program-item.html"
    template_finished = 'finished/program-item.html'

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.time = None


class Assignment(ProgramItem):
    template = "assignment.html"
    template_finished = 'finished/assignment.html'

    def __init__(self, title, duration, assignee=None):
        super(Assignment, self).__init__(title, duration)

        self.assignee = assignee


class StudentsAssignment(Assignment):
    template = "students-assignment.html"
    template_finished = 'finished/student-assignment.html'

    def __init__(self, title, duration, assignee='', partner='partner', point=''):
        super(StudentsAssignment, self).__init__(title, duration, assignee)

        self.partner = partner
        self.point = point


class Section(object):

    def __init__(self, title, items):
        self.title = title
        self.items = items
