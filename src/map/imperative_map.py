# Our company has grown so fast this year so we're giving
# every employee with at least five years of experience an
# extra in their annual salary according to the following table
#    5 years = 5%,
#    6 years: 7.5%,
#    7 years: 10,%
#    8 years: 12.5%
#    9 years: 15%
#    1 years': 20%

import json

with open('src/employees.json') as json_file:
    data = json.load(json_file)

    for i in range(len(data)):
        if data[i]['years_of_experience'] == 5:
            data[i]['annual_salary'] = round(data[i]['annual_salary'] * 1.05, 2)
        if data[i]['years_of_experience'] == 6:
            data[i]['annual_salary'] = round(data[i]['annual_salary'] * 1.075, 2)
        if data[i]['years_of_experience'] == 7:
            data[i]['annual_salary'] = round(data[i]['annual_salary'] * 1.1, 2)
        if data[i]['years_of_experience'] == 8:
            data[i]['annual_salary'] = round(data[i]['annual_salary'] * 1.125, 2)
        if data[i]['years_of_experience'] == 9:
            data[i]['annual_salary'] = round(data[i]['annual_salary'] * 1.15, 2)
        if data[i]['years_of_experience'] == 10:
            data[i]['annual_salary'] = round(data[i]['annual_salary'] * 1.20, 2)

    for i in range(5):
        print(data[i]['id'], data[i]['annual_salary'])
