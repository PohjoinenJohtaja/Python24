players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

middle = len(players) // 2  # индекс середины

first = players[:middle]
second = players[middle:]

print(f"{first}\n{second}")
