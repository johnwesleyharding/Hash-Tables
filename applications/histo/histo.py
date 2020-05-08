import sys

hashtable = {}
doc = ''
ignore = set('" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split())

with open(sys.argv[1]) as f:
    
    for line in f:
        
        value = line.split()
        
        for word in value:
            
            simple = ''.join([char for char in word if char not in ignore]).lower()
            
            if simple not in hashtable:
                
                hashtable[simple] = '#'
                
            else:
                
                hashtable[simple] += '#'

itemlist = list(hashtable.items())
itemlist.sort(key = lambda x: x[1], reverse = True)

for k, v in itemlist:
    print(f'{k:10.9}{v}')