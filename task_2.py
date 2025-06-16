import random

def get_numbers_ticket(min, max, quantity):
    """
    Генерує відсортований список унікальних випадкових чисел у заданому діапазоні.

    :param min: Мінімальне можливе число (не менше 1).
    :param max: Максимальне можливе число (не більше 1000).
    :param quantity: Кількість чисел, які потрібно вибрати.
    :return: Відсортований список унікальних випадкових чисел або пустий список у разі помилки.
    """
    # Перевірка коректності параметрів
    if not (1 <= min <= max <= 1000) or quantity <= 0 or quantity > (max - min + 1):
        return []

    # Генерація унікальних чисел
    numbers = random.sample(range(min, max + 1), quantity)
    
    # Повернення відсортованого списку
    return sorted(numbers)


ticket = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", ticket)