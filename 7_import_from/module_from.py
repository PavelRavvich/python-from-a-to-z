import math, time, os
import random as r
import module
from module import hi
try:
    import nomodule
except ImportError:
    print('ImportError')


print(math.pi)
print(os.uname())
print(time.time())
print(r.random())

sum = module.add(1, 2)
print(sum)

hi()
