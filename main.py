import datetime
'''
 функція вираховує кількість днів між переданою датою в форматі РРРР-ММ-ДД та поточною датою;
    якщо передана дата пізніша за поточну, видається відємне число,
    якщо передане число не є датою в форматі РРРР-ММ-ДД викликається виняток
 вхідний параметр date: рядок, що відображує датау у форматі РРРР-ММ-ДД
 значення, що повертається: ціле число днів
'''
def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        delta = today - input_date
        return delta.days
    except ValueError:
        print("Дата повинна бути у форматі 'РРРР-ММ-ДД'!")

some_date = input("Введіть дату у форматі 'РРРР-ММ-ДД':")
delta_days = get_days_from_today(some_date)
print(f"Різниця між сьогоднішньою датою та введеною = {delta_days}")