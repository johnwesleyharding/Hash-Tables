import math
import random

hashtable = {}

def slowfun(x, y):
    
    if (x, y) in hashtable:
        
        return hashtable(x, y)
    
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653
    
    hashtable(x, y) = v

    return v


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
