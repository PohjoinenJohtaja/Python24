# TODO Напишите функцию find_common_participants
def find_common_participants(line1, line2, separator=","):
    set1 = set(line1.split(separator))
    set2 = set(line2.split(separator))
    return sorted(set1.intersection(set2))


# TODO Провеьте работу функции с разделителем отличным от запятой
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, "|"))

