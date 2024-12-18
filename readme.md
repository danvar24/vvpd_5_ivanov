# Вычисление экспоненциальных и гиперболических функций

Этот Python-скрипт предоставляет функции для вычисления математических выражений с использованием приближений ряда Тейлора. Также в нём реализован простой интерфейс с меню для взаимодействия с пользователем.

---

## Возможности

1. **Экспоненциальная функция (`e^x`)**
    - Вычисляет значение \( e^x \) с использованием приближения ряда Тейлора.
    - Формула: \( e^x = 1 + \frac{x}{1!} + \frac{x^2}{2!} + \cdots + \frac{x^n}{n!} \).

2. **Гиперболический косинус (`ch(x)`)**
    - Вычисляет гиперболический косинус \( \cosh(x) \) с использованием приближения ряда Тейлора.
    - Формула: \( \cosh(x) = 1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \cdots + \frac{x^{2n}}{(2n)!} \).

3. **Натуральный логарифм (`ln(1-x)`)**
    - Вычисляет \( \ln(1-x) \) для \( -1 < x \leq 1 \) с использованием приближения ряда Тейлора.
    - Формула: \( \ln(1-x) = -x - \frac{x^2}{2} - \frac{x^3}{3} - \cdots - \frac{x^n}{n} \).

---

## Установка

1. Склонируйте репозиторий или скачайте скрипт.
2. Убедитесь, что Python (>= 3.x) установлен на вашем компьютере.

---

## Использование

1. Запустите скрипт:
    ```bash
    python script_name.py
    ```

2. Следуйте инструкциям в меню, чтобы выбрать функцию и ввести значения.

### Опции меню

- **1**: Вычислить \( e^x \)
- **2**: Вычислить \( \cosh(x) \)
- **3**: Вычислить \( \ln(1-x) \)
- **4**: Выйти из программы

---

## Функции

### `exponential_function(x, terms=50)`

- **Описание**: Приближённое вычисление \( e^x \) с использованием ряда Тейлора.
- **Аргументы**:
  - `x` (float): Значение \( x \).
  - `terms` (int, optional): Количество членов ряда (по умолчанию: 50).
- **Возвращает**: Приближённое значение \( e^x \).
- **Пример**:
  ```python
  exponential_function(2)  # Возвращает примерно 7.389
  ```

### `hyperbolic_cosine(x, terms=50)`

- **Описание**: Приближённое вычисление \( \cosh(x) \) с использованием ряда Тейлора.
- **Аргументы**:
  - `x` (float): Значение \( x \).
  - `terms` (int, optional): Количество членов ряда (по умолчанию: 50).
- **Возвращает**: Приближённое значение \( \cosh(x) \).
- **Пример**:
  ```python
  hyperbolic_cosine(2)  # Возвращает примерно 3.762
  ```

### `natural_logarithm(x, terms=50)`

- **Описание**: Приближённое вычисление \( \ln(1-x) \) с использованием ряда Тейлора.
- **Аргументы**:
  - `x` (float): Значение \( x \), где \( -1 < x \leq 1 \).
  - `terms` (int, optional): Количество членов ряда (по умолчанию: 50).
- **Возвращает**: Приближённое значение \( \ln(1-x) \).
- **Исключения**: `ValueError`, если \( x \notin (-1, 1] \).
- **Пример**:
  ```python
  natural_logarithm(0.5)  # Возвращает примерно -0.693
  ```

---

## Обработка ошибок

- Проверка вводимых данных гарантирует, что пользователь предоставляет корректные значения.
- Исключения генерируются для недопустимых диапазонов в функции `natural_logarithm` и некорректных входных данных.

---

## Пример взаимодействия

```
Меню функций:
1. e^x (Экспоненциальная функция)
2. ch(x) (Гиперболический косинус)
3. ln(1-x) (Натуральный логарифм)
4. Выход
Выберите функцию (1-4): 1
Введите x (допустимый диапазон: от -бесконечности до +бесконечности): 2
Результат: e^2 = 7.389056098930649
```

---

## Автор
Разработчик: **[Иванов Даниил Олегович и Батюта Александр Владимирович ]**

---
