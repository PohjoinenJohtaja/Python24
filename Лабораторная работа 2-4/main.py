from abc import ABC, abstractmethod


class Microcontroller(ABC):
    """
    Базовый класс - микроконтроллеры.
    """

    def __init__(self, model: str, architecture: str, pins: int):
        """
        Ининциализация объекта "микроконтроллер"

            :param model (str): Модель микроконтроллера
            :param architecture (str): Архитектура микроконтроллера
            :param pins (int): Количество GPIO пинов микроконтроллера

        """
        if not isinstance(model, str):
            raise TypeError("Модель микроконтроллера должна быть строкой")
        self.model = model
        if not isinstance(model, str):
            raise TypeError("Название архитектуры микроконтроллера должно быть строкой")
        self.architecture = architecture
        if not isinstance(pins, int):
            raise TypeError("Количетство пинов должено быть целым числом")
        if pins < 0:
            raise ValueError("Количество пинов не может быть меньше 0")
        self.pins = pins

    def __str__(self):
        """
        Возвращает информауию о микроконтроллере в виде строки
        """
        return f"{self.model} - Architecture: {self.architecture}, Pins: {self.pins}"

    def __repr__(self):
        """
        Возвращает детальтную информауию о микроконтроллере в виде строки
        """
        return f"Microcontroller(model={self.model}, architecture={self.architecture}, pins={self.pins})"

    @abstractmethod
    def program(self, code: str):
        """
        Абстрактный метод программирования микроконтроллера

            :param code (str): Код, который необходимо запрограммировать в микроконтроллер
        """
        pass


class AVR(Microcontroller):
    """
    Дочерний класс, представляющий микроконтроллер семейство AVR
    """

    def __init__(self, model: str, pins: int, frequency: int):
        """
        Ининциализация AVR микроконтроллера

            :param model (str): Модель микроконтроллера
            :param pins (int): Количество GPIO пинов микроконтроллера
            :param frequency (int): Рабрчая частота микроконтроллера, Гц
        """
        super().__init__(model, "AVR", pins)
        if not isinstance(frequency, int):
            raise TypeError("Частота тактирования должна быть целым числом")
        if frequency < 0:
            raise ValueError("Частота тактирования не может быть меньше 0")
        self.frequency = frequency

    def __str__(self):
        """
        Возвращает информауию о микроконтроллере в виде строки
        """
        return super().__str__() + f", Frequency: {self.frequency} Hz"

    def __repr__(self):
        """
        Возвращает детальтную информауию о микроконтроллере в виде строки
        """
        return f"AVR(model={self.model}, pins={self.pins}, frequency={self.frequency})"

    def program(self, code: str):
        """
        Программирование микроконтроллера AVR с помощью предоставленного кода

            :param code (str): Код, который необходимо запрограммировать в микроконтроллер
        Этот метод перегружен для конкретной реализации программирования AVR микроконтроллера

        Возвращает:
            :bool: 1 (Истина), если програмирование прошло успешно, и 0 (Ложь) в случае неуспеха
        """
        # Условная реализация программирования выделенного микроконтроллера (AVR).
        return True


if __name__ == "__main__":
    MC = AVR("ATmega 328p", 23, 16 * 1000 * 1000)
    MC.program("Put your code right here")
    print(MC)
