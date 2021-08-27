# We're going to calculate the years of experience that
# we made up with all the employees

import json

with open('src/employees.json') as json_file:
    data = json.load(json_file)

    total_years = 0

    for emp in data:
        total_years += emp['years_of_experience']

    print(total_years)
