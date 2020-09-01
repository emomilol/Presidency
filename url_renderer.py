import datetime
import locale

locale.setlocale(locale.LC_ALL, 'de_DE')

template = 'https://www.jw.org/de/publikationen/jw-arbeitsheft/{month}-{year}-mwb/' # programm-fuer-{start_day}{start_month}-{end_day}{end_month}/'

REPLACEMENTS =  {
    'sep': 'sept',
    'mae': 'maerz',
    'jun': 'juni',
}

def month_abbreviation(month):
    abbr = month[:3]
    return REPLACEMENTS.get(abbr, abbr)


def get_current_url():
    start = datetime.datetime.today()
    while start.weekday() > 0:
        start -= datetime.timedelta(days=1)

    month = start.strftime("%B").lower().replace('ä', 'ae')
    year = start.year
    start_day = start.day

    end = start + datetime.timedelta(days=6)
    end_month = end.strftime("%B").lower().replace('ä', 'ae')
    end_day = end.day

    start_month = "" if month == end_month else month

    return template.format(
        month=month,
        year=year,
        start_day=start_day,
        start_month=month_abbreviation(start_month),
        end_month=month_abbreviation(end_month),
        end_day=end_day
    )
