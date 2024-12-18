import doctest


class Vehicle:
    def __init__(self, brand: str, model: str, year: int):
        """
        Создание и подготовка к работе объекта "Транспортное средство"

        :param brand: Бренд транспортного средства (должен быть непустой строкой).
        :param model: Модель транспортного средства (должна быть непустой строкой).
        :param year: Год выпуска (должен быть положительным целым числом).

        :raise ValueError: Если brand или model пустые, или year не положительный.

        >>> car = Vehicle("Toyota", "Camry", 2020)
        """

        if not brand:
            raise ValueError("Бренд не может быть пустым.")
        if not model:
            raise ValueError("Модель не может быть пустой.")
        if year <= 0:
            raise ValueError("Год выпуска должен быть положительным числом.")

        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self) -> None:
        """
        Запускает двигатель транспортного средства.

        >>> car = Vehicle("Toyota", "Camry", 2020)
        >>> car.start_engine()
        """
        ...

    def stop_engine(self) -> None:
        """
        Останавливает двигатель транспортного средства.

        >>> car = Vehicle("Toyota", "Camry", 2020)
        >>> car.stop_engine()
        """
        ...

    def drive(self, distance: float) -> None:
        """
        Двигает транспортное средство на заданное расстояние.

        :param distance: Расстояние в километрах (должно быть неотрицательным числом).

        :raise ValueError: Если distance отрицательное.

        >>> car = Vehicle("Toyota", "Camry", 2020)
        >>> car.drive(100.0)
        """
        
        if distance <= 0:
            raise ValueError("Расстояние должно быть положительным числом.")        
        ...


class Wardrobe:
    def __init__(self, material: str, height: float, width: float):
        """
        Создание и подготовка к работе объекта "Шкаф".

        :param material: Материал шкафа (должен быть непустой строкой).
        :param height: Высота шкафа в сантиметрах (должна быть положительным числом).
        :param width: Ширина шкафа в сантиметрах (должна быть положительным числом).

        :raise ValueError: Если material пустой или height/width не положительные.

        >>> wardrobe = Wardrobe("Дерево", 200.0, 100.0)
        """

        if not material:
            raise ValueError("Материал не может быть пустым.")
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом.")
        if width <= 0:
            raise ValueError("Ширина должна быть положительным числом.")

        self.material = material
        self.height = height
        self.width = width

    def open_door(self) -> None:
        """
        Открывает дверь шкафа.

        >>> wardrobe = Wardrobe("Дерево", 200.0, 100.0)
        >>> wardrobe.open_door()
        """
        ...

    def close_door(self) -> None:
        """
        Закрывает дверь шкафа.

        >>> wardrobe = Wardrobe("Дерево", 200.0, 100.0)
        >>> wardrobe.close_door()
        """
        ...

    def store_item(self, item: str) -> None:
        """
        Сохраняет предмет в шкафу.

        :param item: Имя предмета (должно быть непустой строкой).

        :raise ValueError: Если item пустой.

        >>> wardrobe = Wardrobe("Дерево", 200.0, 100.0)
        >>> wardrobe.store_item("Платье")
        """

        if not item:
            raise ValueError("Название вещи не может быть пустым.")
        ...


class Group:
    def __init__(self, name: str, member_count: int, purpose: str):
        """
        Создание и подготовка к работе объекта "Группа".

        :param name: Название группы (должно быть непустой строкой).
        :param member_count: Количество участников группы (должно быть неотрицательным целым числом).
        :param purpose: Цель группы (должна быть непустой строкой).

        :raise ValueError: Если name или purpose пустые, или member_count отрицательный.

        >>> group = Group("Спортсмены", 10, "Тренировки")
        """

        if not name:
            raise ValueError("Название группы не может быть пустым.")
        if member_count < 0:
            raise ValueError("Количество участников не может быть отрицательным.")
        if not purpose:
            raise ValueError("Цель группы не может быть пустой.")

        self.name = name
        self.member_count = member_count
        self.purpose = purpose

    def add_member(self) -> int:
        """
        Добавляет участника в группу.

        :return: Обновленное количество участников группы.

        >>> group = Group("Спортсмены", 10, "Тренировки")
        >>> group.add_member()
        11
        """
        ...

    def remove_member(self) -> int:
        """
        Удаляет участника из группы.

        :return: Обновленное количество участников группы.

        >>> group = Group("Спортсмены", 10, "Тренировки")
        >>> group.remove_member()
        9
        """
        ...

    def change_purpose(self, new_purpose: str) -> None:
        """
        Изменяет цель группы.

        :param new_purpose: Новая цель группы (должна быть непустой строкой).

        :raise ValueError: Если new_purpose пустая.

        >>> group = Group("Спортсмены", 10, "Тренировки")
        >>> group.change_purpose("Соревнования")
        """

        if not new_purpose:
            raise ValueError("Название цели не может быть пустым.")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
