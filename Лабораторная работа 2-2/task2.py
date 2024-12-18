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


class Library:
    def __init__(self, books=None):
        """
        Конструктор класса Library.

        :param books: Список книг (по умолчанию пустой список).
        """

        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Возвращает следующий идентификатор для добавления новой книги.

        :return: Идентификатор книги.
        """

        if not self.books:
            return 1
        else:
            return max(book.id for book in self.books) + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги по её идентификатору.

        :param book_id: Идентификатор книги.
        :return: Индекс книги в списке.

        :raise ValueError: Если книга с данным идентификатором не найдена.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
