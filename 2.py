import datetime


def validate_date(date_text: str) -> bool:
    try:
        datetime.datetime.strptime(date_text, "%d.%m.%Y")
        return True
    except ValueError:
        return False


date = input('Введите дату: ')

print(validate_date(date))