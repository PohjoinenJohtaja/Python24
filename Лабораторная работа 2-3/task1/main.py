class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        """
        Ининциализация объекта "Book"

            :param name (str): Название книги
            :param author (str): Имя автора

        """
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть строкой")
        self._name = name

        if not isinstance(author, str):
            raise TypeError("Имя автора должно быть строкой")
        self._author = author

    def name(self):
        return self._name

    def author(self):
        return self._author

    def __str__(self):
        return f"Книга '{self._name}', Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """ Дочерний класс для бумажной книги. """

    def __init__(self, name: str, author: str, pages: int):
        """
        Ининциализация объекта "AudioBook"

            :param name (str): Название книги
            :param author (str): Имя автора
            :param pages (int): Количество страниц книги

        """
        super().__init__(name, author)
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = pages

    def pages(self):
        return self._pages

    def pages(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()}, Страниц: {self._pages}"

    def __repr__(self):
        return f"{super().__repr__()}, pages={self._pages!r})"


class AudioBook(Book):
    """ Дочерний класс для аудиокниги. """

    def __init__(self, name: str, author: str, duration: float):
        """
        Ининциализация объекта "AudioBook"

            :param name (str): Название книги
            :param author (str): Имя автора
            :param duration (float): Длительность аудиокниги

        """
        super().__init__(name, author)
        if not isinstance(duration, (float, int)) or duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = duration

    def duration(self):
        return self._duration

    def duration(self, value: float):
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = float(value)

    def __str__(self):
        return f"{super().__str__()}, Продолжительность: {self._duration} ч."

    def __repr__(self):
        return f"{super().__repr__()}, duration={self._duration!r})"


if __name__ == "__main__":
    Book = PaperBook("Война и мир", "Толстой Л. Н.", 5202)
    print(Book)

    Book = AudioBook("Война и мир", "Толстой Л. Н.", 5)
    print(Book)
