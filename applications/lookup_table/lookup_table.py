import math
import random

speed = {}
def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster
    #speed = {}
    key = str(x) + str(y)
    #print(key)
    #print(speed)
    try:
        cashed_v = speed[key]
        #print(speed)
        return cashed_v
    except KeyError:
        #print("no match")

        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653

        speed[key] = v
        return v


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
