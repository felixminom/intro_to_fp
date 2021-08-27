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

    for emp in data:
        if emp['years_of_experience'] == 5:
            emp['annual_salary'] = round(emp['annual_salary'] * 1.05, 2)
        if emp['years_of_experience'] == 6:
            emp['annual_salary'] = round(emp['annual_salary'] * 1.075, 2)
        if emp['years_of_experience'] == 7:
            emp['annual_salary'] = round(emp['annual_salary'] * 1.1, 2)
        if emp['years_of_experience'] == 8:
            emp['annual_salary'] = round(emp['annual_salary'] * 1.125, 2)
        if emp['years_of_experience'] == 9:
            emp['annual_salary'] = round(emp['annual_salary'] * 1.15, 2)
        if emp['years_of_experience'] == 10:
            emp['annual_salary'] = round(emp['annual_salary'] * 1.20, 2)

    for i in range(5):
        print(data[i]['id'], data[i]['annual_salary'])
