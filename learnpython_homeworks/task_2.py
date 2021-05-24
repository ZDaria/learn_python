

def string_comp(string_1, string_2):
    if type(string_1) == str and type(string_2) == str:
        if len(string_1) == len(string_2):
            return 1
        elif len(string_1) > len(string_2) and string_2 != "learn":
            return 2
        elif string_2 == "learn":
            return 3
    else:
        return 0


print(string_comp("string", 1))
print(string_comp(1, "learn"))
print(string_comp("same string", "same string"))
print(string_comp("this string is bigger", "little string"))
print(string_comp("this string is bigger", "learn"))


def test_return_0():
    """ Проверить, является ли то, что передано функции, строками. Если нет - вернуть 0 """
    assert 0 == string_comp("string", 1)


def test_return_0_with_learn():
    assert 0 == string_comp(1, "learn")


def test_return_1():
    """Если строки одинаковые, вернуть 1"""
    assert 1 == string_comp("same string", "same string")


def test_return_2():
    """Если строки разные и первая длиннее, вернуть 2"""
    assert 2 == string_comp("this string is bigger", "little string")


def test_return_3():
    """Если строки разные и вторая строка 'learn', вернуть 3 """
    assert 3 == string_comp("this string is bigger", "learn")


def test_second_string_is_bigger():
    assert 2 == string_comp("little string", "this string is bigger")
