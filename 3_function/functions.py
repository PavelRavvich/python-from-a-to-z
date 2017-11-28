def func(x, y):
    return x + y


print(func(12, 13))


def func1(x):
    def func2(y):
        return x + y

    return func2


f1 = func1(100)
res = f1(200)
print(res)

print(func1(100)(300))


# Если функция ничего не возвращает то используется pass
def func3():
    x = 5
    pass


# Аргумент по умолчанию.
def func4(x, pow=2):
    return x ** pow


print(func4(3))


# Переменное колличество аргументов.
def func5(*args):  # С одной * приходит кортеж (не изменяемый)
    return args


print(func5(3, 6))


def func6(**args):  # Словарь
    return args


print(func6(a='a', b='b'))


# Lambda expression
add = lambda x, y: x + y
print(add(3,2))
