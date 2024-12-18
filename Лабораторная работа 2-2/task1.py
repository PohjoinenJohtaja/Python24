BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Конструктор класса Book.

        :param id_: Идентификатор книги (должен быть положительным целым числом).
        :param name: Название книги (не должно быть пустой строкой).
        :param pages: Количество страниц в книге (должно быть положительным целым числом).

        :raise ValueError: Если id_ не положительный, name пустой или pages не положительное.

        >>> book = Book(1, 'test_name_1', 200)
        """

        if id_ <= 0:
            raise ValueError("Идентификатор книги должен быть положительным числом.")
        if not name:
            raise ValueError("Название книги не может быть пустым.")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")

        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.

        :return: Строка формата "Книга 'название_книги'".

        >>> book = Book(1, 'test_name_1', 200)
        >>> str(book)
        "Книга 'test_name_1'"
        """

        return f"Книга '{self.name}'"

    def __repr__(self) -> str:
        """
        Возвращает валидную строку для создания экземпляра класса Book.

        :return: Строка формата Book(id_=id, name='name', pages=pages).

        >>> book = Book(1, 'test_name_1', 200)
        >>> repr(book)
        "Book(id_=1, name='test_name_1', pages=200)"
        """

        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
