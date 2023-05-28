#Name: Tamir David

from datetime import datetime

def gen_secs():
    for second in range(60):
        yield second

def gen_minutes():
    for minute in range(60):
        yield minute

def gen_hours():
    for hour in range(24):
        yield hour

def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield f"{hour:02d}:{minute:02d}:{second:02d}"

def gen_years(start=datetime.now().year):
    current_year = start
    while True:
        yield current_year
        current_year += 1

def gen_months():
    for month in range(1, 13):
        yield month

def gen_days(month, leap_year=True):
    days_in_month = {
        1: 31,
        2: 29 if leap_year else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    yield days_in_month[month]

def gen_date():
    count = 0
    date_gen = (date for date in gen_date_inner())

    while True:
        count += 1
        if count % 1000000 == 0:
            print(next(date_gen))
        else:
            next(date_gen)

def gen_date_inner():
    for year in gen_years():
        leap_year = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

        for month in gen_months():
            days_in_month = next(gen_days(month, leap_year))

            for day in range(1, days_in_month + 1):
                for hour in gen_hours():
                    for minute in gen_minutes():
                        for second in gen_secs():
                            yield f"{day:02d}/{month:02d}/{year} {hour:02d}:{minute:02d}:{second:02d}"

gen_date()


