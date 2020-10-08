import datetime
import locale

locale.setlocale(locale.LC_ALL, 'es_ES')

template = 'https://www.jw.org/es/biblioteca/guia-actividades-reunion-testigos-jehova/{month}-{year}-mwb/Programa-para-la-reunión-Vida-y-Ministerio-{start_day}{start_month}-a-{end_day}-de-{end_month}-de-{year}/' # programm-fuer-{start_day}{start_month}-{end_day}{end_month}/'

def month_abbreviation(month):
    return month[:3]


def get_current_url():
    start = datetime.datetime.today()
    while start.weekday() > 0:
        start -= datetime.timedelta(days=1)

    month = start.strftime("%B").lower()
    year = start.year
    start_day = start.day

    end = start + datetime.timedelta(days=6)
    end_month = end.strftime("%B").lower().replace('ä', 'ae')
    end_day = end.day

    start_month = "" # if month == end_month else month

    return template.format(
        month=month,
        year=year,
        start_day=start_day,
        start_month=start_month,
        end_month=end_month,
        end_day=end_day
    )
