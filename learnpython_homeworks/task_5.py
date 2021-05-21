# 1


def hello_user():
    mark = 0
    while True:
        try:
            answer = input("Как дела? ")
        except KeyboardInterrupt:
            print("Пока!")
            break


hello_user()


# 2

def discounted(price, discount, max_discount):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = int(max_discount)
        if max_discount > 99:
            raise ValueError("Слишком большая максимальная скидка")
        if discount >= max_discount:
            return price
        else:
            return price - price * discount / 100
    except ValueError:
        print("Вы ввели не верное число")
    except TypeError:
        print("Введеное значение не является числом")


print(discounted(10, 5, "er"))

