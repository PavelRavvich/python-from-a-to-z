# Словари просто мапа.

# Первый способ создания в фигурных скобках
a = {1:'hello', 2: "world"}
print(a)
print(a.get(2))

# Второй способ создания с помощю dict()
b = dict(first='1', second='2')
b['first'] = 'update'
print(b)

# Третий способ создания в с помощью dict.fromkeys([])
# Создание кортежа с ключами но без значений (None)
d = dict.fromkeys(['key_1', 'key_2'])
print(d)
# Создание кортежа с разными ключами и одинаковыми значениями.
e = dict.fromkeys(['key_1', 'key_2'], 'common_value')
print(e)

# Четвертый способ при помощи цикла.
c = {a : a ** 2 for a in range(7)}
print(c)

# пример применения.
person = {'name' : {'first_name' : 'Ivan', 'last_name' : 'Petrovich'}, 'address' : ['Moscow', 'St. Lenin']}
print(person)
print(person['name'])
print(person['name']['last_name'])

# Получить ключи.
print(person.keys())
# Получить все значения
print(person.values())