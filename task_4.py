from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    """
    Повертає список користувачів, яких потрібно привітати з днем народження
    протягом 7 днів включно з сьогоднішнім днем.

    Якщо день народження припадає на вихідний (субота або неділя),
    дата привітання переноситься на наступний понеділок.
    """
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Перетворюємо дату народження в об'єкт datetime.date
        birth_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Створюємо дату народження на поточний рік
        birthday_this_year = birth_date.replace(year=today.year)

        # Якщо день народження вже був цього року, дивимось наступного року
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Різниця між днем народження і сьогоднішнім днем
        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days <= 7:
            # Перевіряємо, чи припадає на вихідний
            congratulation_date = birthday_this_year
            if congratulation_date.weekday() == 5:  # Субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # Неділя
                congratulation_date += timedelta(days=1)

            # Додаємо у список
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# --- Приклад використання ---

users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.06.20"},
        {"name": "Alex Johnson", "birthday": "1980.03.28"},
        {"name": "Марія Коваленко", "birthday": "1993.06.21"},
    ]

result = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", result)