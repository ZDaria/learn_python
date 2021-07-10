name = "Дарья"
print("Привет, %s" % name)
print(f"Привет, {name}")
print("Привет,", name)
print("Привет, " + name)

# strings
a = " Привет"
b = "мир"
a == b
print(a + b)
print(a + " " + b + "!")
c = '{} {}!'.format(a, b)
print(c)
c = 2
#d = a + ' ' + b + c + '!'
d = '{} {}{}!'.format(a, b, c)
print(d)

# string formatting
# first var
user = 'Миша'
b = 'Привет {name2}!'.format(name2=user)
print(b)
# second var
b = f'Привет {user}!'
print(b)

# string length
b = 'мир '
c = f'{a} {b}!'
print(len(c))
print(c.upper())
print(c.lower())
print(c.capitalize())
print(c.strip())

# replace in the string
