# age


def get_user_occupation(years_old):
    if 2 <= years_old <= 6:
        return "Детский сад"
    elif 6 < years_old <= 18:
        return "Школа"
    elif 18 < years_old <= 24:
        return "ВУЗ"
    elif 24 < years_old <= 80:
        return "Работа"
    elif years_old < 2 or years_old > 80:
        return "Дом"


age = input("Сколько Вам полных лет? ")

user_occupation = get_user_occupation(int(age))
print(f"Ваш род занятий: {user_occupation}")
