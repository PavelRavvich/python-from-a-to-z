#Кортежи - константы в круглых скобках или просто через запятую. Не изменяемы.
a = (76, 38, 78, 78)
c = 23, 54, 2
print(a)
print(a.__sizeof__())
print(c)
print(c.__sizeof__())



b = tuple("Hello world")
print(b)


print(a.count(38))