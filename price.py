# example
price1 = 100
discount1 = 10


def discounted(price, discount, max_discount=20):
    price = abs(float(price))
    discount = abs(float(discount))
    if max_discount > 99:
        raise ValueError("Слишком большая максимальная скидка")
    if discount >= max_discount:
        return price
    else:
        return price - price * discount / 100


print(discounted(price1, discount1))
print(discounted(200, 5))
print(discounted(100, 180))

# Task 1
# 1.1


def get_sum(one, two, delimetr='&'):
    return f"{str(one)} {delimetr} {str(two)}".upper()


test1 = get_sum("Python", "Learn")
# 1.2
print(test1)
# 1.3
print(test1)

# Task 2
# 2.1


def format_price(price):
    price = int(price)  # 2.3
    return f"Цена: {price} руб"  # 2.4


price_rub = format_price(56.24)  # 2.5
print(price_rub)  # 2.6

