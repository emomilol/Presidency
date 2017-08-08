import datetime
import locale

locale.setlocale(locale.LC_ALL, 'de_DE')

template = 'https://www.jw.org/de/publikationen/jw-arbeitsheft/{month}-{year}-mwb/programm-fuer-{start_day}{start_month}-{end_day}{end_month}/'

def get_current_url():
    start = datetime.datetime.today()
    while start.weekday() > 0:
        start -= datetime.timedelta(days=1)

    month = start.strftime("%B").lower()
    year = start.year
    start_day = start.day

    end = start + datetime.timedelta(days=6)
    end_month = end.strftime("%B").lower()
    end_day = end.day

    start_month = "" if month == end_month else month

    return template.format(
        month=month,
        year=year,
        start_day=start_day,
        start_month=start_month[:3],
        end_month=end_month[:3],
        end_day=end_day
    )
