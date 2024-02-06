from datetime import datetime, timedelta

users = {
    'Anna': '15-03-1990',
    'Bartek': '22-07-1985',
    'Katarzyna': '10-11-1995',
    'Piotr': '05-04-1980',
    'Magda': '18-09-1992',
    'Miłosz': '10-02-2004'
}
def get_birthdays_per_week(users):
    today = datetime.now()
    week = timedelta(weeks=1)

    birthdays_this_week = []

    for i in users:
        users[i] = datetime.strptime(users[i], '%d-%m-%Y').replace(year=today.year)

        if users[i] - today <= week:
            birthdays_this_week.append((i, users[i]))

    grouped_birthdays = {}
    for name, day in birthdays_this_week:
        weekday = day.strftime('%A')
        if weekday in grouped_birthdays:
            grouped_birthdays[weekday].append(name)
        else:
            grouped_birthdays[weekday] = [name]
    print(grouped_birthdays)
    for day, names in grouped_birthdays.items():
        print(f'{day}: {", ".join(names)}')
get_birthdays_per_week(users)