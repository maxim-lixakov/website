import json
from . import models


def dump_data(data):
    login = '+79771301704'
    run_dates = {}
    year, month = '', ''
    # with open("plan.json", "r") as f:
    #     DATA = json.load(f)

    DATA = data
    months = {"01": "январь", "02": "февраль", "03": "март",
              "04": "апрель", "05": "май", "06": "июнь",
              "07": "июль", "08": "август", "09": "сентябрь",
              "10": "октябрь", "11": "ноябрь", "12": "декабрь"}

    for key in DATA["run"]:
        if key[:4] in run_dates:
            if months[key[5:7]] in run_dates[key[:4]]:
                run_dates[key[:4]][months[key[5:7]]].append(key[8:10])
            else:
                run_dates[key[:4]].update({months[key[5:7]]: [key[8:10]]})
        else:
            run_dates[key[:4]] = {months[key[5:7]]: []}
            run_dates[key[:4]][months[key[5:7]]].append(key[8:10])
    user = models.User.objects.get(login=login)
    for year in run_dates:
        for month in run_dates[year]:
            for day in run_dates[year][month]:
                for number in months:
                    if months[number] == month:
                        date = year + "-" + number + "-" + day
                        break
                date = year + "-" + number + "-" + day
                user.user_data_set.create(year=year,
                                          day=day,
                                          month=month,
                                          text=DATA["run"][date][0])

    return 'OK'

