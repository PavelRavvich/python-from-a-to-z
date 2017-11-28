listItems = [1, "list", ['d', 1.3]]

print(listItems)

# Добавление в конец списка.
listItems.append(23)
listItems.append("row")

print(listItems)

# Добавление одного списка в конец другого.
listItems.extend([1, 2, 3])
print(listItems)

# Вставка по интдексу
listItems.insert(0, "insert")
print(listItems)

# Удаление первого элемента с значением x. Если не такого найдется - error.
x = 1
listItems.remove(1)
print(listItems)

# Удаление элемента индексу и возвращает его.
firstVal = listItems.pop(0)
print(firstVal)
# Если ничего не указать то будет выбран последний элемент.
print(listItems.pop())

# Получение индекса по значению.
print(listItems.index(23))

# Получить колличество элементов с заданным значением.
print(listItems.count(23))

#  Сортировка на основе функции.
l = [4, 2, 7, 1, 3, 6, 5]
print(l)
l.sort()
print(l)
# Разворот списка в обратном направлении.
l.reverse()
print(l)
# Очистка списка
l.clear()
print(l)
