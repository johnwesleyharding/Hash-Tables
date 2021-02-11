"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)

def f(x):
    return x * 4 + 6

r = [f(x) for x in q[-1::-1]]

hash_sum, hash_dif = {}, {}

l = len(r)

for i in range(l):
    
    a = r[i]
    
    for j in range(i, l):
        
        b = r[j]
        
        hash_sum[(a, b)] = a + b
        hash_sum[(b, a)] = b + a
        hash_dif[(a, b)] = a - b
        
for k, v in hash_sum.items():
    
    for k2, v2 in hash_dif.items():
        
        if v == v2:
            
            print(f'{k[0]} + {k[1]}  =  {v}  =  {k2[0]} - {k2[1]}')