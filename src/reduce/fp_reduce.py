# We're going to calculate the years of experience that
# we made up with all the employees

import json
import functools

with open('src/employees.json') as json_file:
    data = json.load(json_file)

    total_years = functools.reduce(
        lambda acc, emp: acc + emp['years_of_experience'], data, 0
    )

    print(total_years)
