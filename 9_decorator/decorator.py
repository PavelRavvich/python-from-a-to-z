def first_decorator(func):
    def wrapper():
        print('Before first decorator')
        func()
        print('After first decorator')

    return wrapper


def second_decorator(func):
    def wrapper():
        print('Before second decorator')
        func()
        print('After second decorator')

    return wrapper


@first_decorator
@second_decorator
def show():
    print('Base func call')


show()

print('==========================')

def show1():
    print('Base func call')

first_dec = first_decorator(show1)
first_dec()
