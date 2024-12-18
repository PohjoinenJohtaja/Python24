# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44 * 1024 * 1024  # объём дискеты
pages = 100
lines = 50
symbols = 25
symbol = 4

number = volume / pages / lines / symbols / symbol

print("Количество книг, помещающихся на дискету:", int(number))
