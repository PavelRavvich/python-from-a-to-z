try:
    print(10 / 0)
except ZeroDivisionError:
    print('ZeroDivisionError')
finally:
    print('finally')