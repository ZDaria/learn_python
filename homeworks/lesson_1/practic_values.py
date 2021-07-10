v = input('Введите число от 1 до 10: ')
try:
    if int(v) < 1 or int(v) > 10:
        raise ValueError
    print(int(v) + 10)
except ValueError:
    print(f"{v} не входит в указанный промежуток")
except:
    print(f"{v} - это не число")

name = input("Введите ваше имя: ").upper()
print(f"Привет, {name}! Как дела?")

print(float("1"))
print(int('2'))
print(bool(1))
print(bool(''))
print(bool(0))
