# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(csv_path, json_path, delimiter=',', newline='\n'):
    # TODO считать содержимое csv файла
    with open(csv_path, 'r', newline=newline) as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        json_data = [row for row in reader]

    # TODO Сериализовать в файл с отступами равными 4
    with open(json_path, 'w') as file:
        file.write(json.dumps(json_data, indent=4))


if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
