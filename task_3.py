import re

def normalize_phone(phone_number):
    """
    Нормалізує телефонний номер до міжнародного формату.
    Видаляє всі символи, крім цифр і '+', і додає префікс '+38' у разі потреби.

    :param phone_number: Рядок із телефоном у довільному форматі.
    :return: Нормалізований номер телефону у форматі +380XXXXXXXXX
    """
    # Видаляємо всі символи, крім цифр
    digits_only = re.sub(r'\D', '', phone_number)

    # Якщо номер починається з '380', додаємо '+'
    if digits_only.startswith('380'):
        return '+' + digits_only

    # Якщо номер починається з '0', додаємо '+38' перед ним
    if digits_only.startswith('0'):
        return '+38' + digits_only

    # Якщо вже має правильний міжнародний формат (наприклад, +380...), просто повертаємо
    if phone_number.strip().startswith('+'):
        cleaned = '+' + re.sub(r'\D', '', phone_number)
        return cleaned

    # Якщо інший формат — вважаємо, що треба додати '+38'
    return '+38' + digits_only


# --- Основна частина програми ---
raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)