# TODO решите задачу
import json


def task(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    summ = 0

    for item in data:
        summ += item['score'] * item['weight']

    return round(summ, 3)


print(task('input.json'))
