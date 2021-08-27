import json

with open('src/employees.json') as json_file:
    data = json.load(json_file)

    # 1. let's get all employees with less than 3 years
    # of experience

    employees_filtered = []

    for i in range(len(data)):
        if data[i]['years_of_experience'] <= 3:
            employees_filtered.append(data[i])

    print(f'Employees with less than 3 years of experience:{len(employees_filtered)}')

    # 2. let's get all employees with less than 3 years of experience
    # and less than 25 years

    employees_3_years_and_25_years = []

    for i in range(len(data)):
        if data[i]['years_of_experience'] <= 3 and data[i]['age'] <= 25:
            employees_3_years_and_25_years.append(data[i])

    print(f'''Employees with less than 3 years of experience
        and less than 25 years:{len(employees_3_years_and_25_years)}''')

    # 3. let's get all employees that don't have a shirt size :(

    employees_with_no_shirt_size = []

    for i in range(len(data)):
        if not data[i]['shirt_size']:
            employees_with_no_shirt_size.append( data[i])

    print(f'Employees with no shirt size:{len(employees_with_no_shirt_size)}')
