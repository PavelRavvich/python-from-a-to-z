i = 0
while i < 5:
    print("while iteration =", i + 1)
    i += 1

for j in "hello_world":
    # continue для пропуска итерации.
    if j == "l":
        continue
    # break выход из цикла.
    if j == "w":
        break

    print("symbol:", j)


# else для циклов.
for j in "hello":
    if j == "a":
        break
    print(j)
else:
    print("Если break не сработал, то сработает else")

