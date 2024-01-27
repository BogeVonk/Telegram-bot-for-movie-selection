import datetime


def get_welcome() -> str:
    curent_time = datetime.datetime.now()
    if 0 <= curent_time.hour < 5:
        return "Доброй ночи!"
    if 5 <= curent_time.hour < 12:
        return "Доброе утро!"
    if 12 <= curent_time.hour < 16:
        return "Добрый день!"
    else:
        return "Добрый вечер!"
