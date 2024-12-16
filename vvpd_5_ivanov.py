import math


def exponential_function(x, terms=50):


    """
    Краткое описание:
        Вычисляет гиперболический косинус ch(x) с использованием ряда Тейлора.

    Подробное описание:
        Разложение гиперболического косинуса в ряд Тейлора имеет вид:
            ch(x) = 1 + x^2/2! + x^4/4! + ... + x^(2n)/(2n)!
        Суммирование выполняется до заданного количества членов.

    Аргументы:
        x (float): Значение аргумента, для которого нужно вычислить ch(x).
        terms (int, optional): Количество членов ряда. По умолчанию 50.

    Возвращаемое значение:
        float: Приближённое значение ch(x).

    Исключения:
        - `ValueError`: если terms <= 0.

    Пример использования:
        >>> hyperbolic_cosine(2)
        3.7621956910836314
        >>> hyperbolic_cosine(0)
        1.0
    """

    result = 0
    for n in range(terms):
        result += (x ** n) / math.factorial(n)
    return result


def hyperbolic_cosine(x, terms=50):
    """
    Краткое описание:
        Вычисляет гиперболический косинус ch(x) с использованием ряда Тейлора.

    Подробное описание:
        Разложение гиперболического косинуса в ряд Тейлора имеет вид:
            ch(x) = 1 + x^2/2! + x^4/4! + ... + x^(2n)/(2n)!
        Суммирование выполняется до заданного количества членов.

    Аргументы:
        x (float): Значение аргумента, для которого нужно вычислить ch(x).
        terms (int, optional): Количество членов ряда. По умолчанию 50.

    Возвращаемое значение:
        float: Приближённое значение ch(x).

    Исключения:
        - `ValueError`: если terms <= 0.

    Пример использования:
        >>> hyperbolic_cosine(2)
        3.7621956910836314
        >>> hyperbolic_cosine(0)
        1.0
    """
    result = 0
    for n in range(terms):
        result += (x ** (2 * n)) / math.factorial(2 * n)
    return result


def get_input(prompt, validation_func):
    """Получает ввод от пользователя с валидацией."""
    while True:
        try:
            value = float(input(prompt))
            if validation_func(value):
                return value
            else:
                print("Введено некорректное значение. Попробуйте ещё раз.")
        except ValueError:
            print("Ошибка: введите числовое значение.")


def main():
    while True:
        print("\nМеню функций:")
        print("1. e^x (Экспоненциальная функция)")
        print("2. ch(x) (Гиперболический косинус)")
        print("4. Выход")

        choice = input("Выберите функцию (1-4): ")
        if choice == '1':
            x = get_input("Введите x (допустимый диапазон: от -бесконечности до +бесконечности): ", lambda v: True)
            print(f"Результат e^{x} = {exponential_function(x)}")
        elif choice == '2':
            x = get_input("Введите x (допустимый диапазон: от -бесконечности до +бесконечности): ", lambda v: True)
            print(f"Результат ch({x}) = {hyperbolic_cosine(x)}")
        elif choice == '4':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
