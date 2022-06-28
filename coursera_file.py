#! /usr/bin/env python3

import csv


def read_employees(csv_file_location):
    with open(csv_file_location) as file:
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        employee_file = csv.DictReader(file, dialect='empDialect')
        employee_list = []
        for data in employee_file:
            employee_list.append(data)
        return employee_list


path = input(r'Path: ')
employee_list = read_employees(path)


def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(
            department_name)
    return department_data


dictionary = process_data(employee_list)


def write_report(dictionary, report_file):
    with open(report_file, 'w+') as file:
        for keys in sorted(dictionary):
            file.write(str(keys) + ':' + str(dictionary[keys] + '\n'))
        file.close()


report_path = input(r'Path: ')
write_report(dictionary, report_path)
