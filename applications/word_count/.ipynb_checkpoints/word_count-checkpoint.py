ignore = set('" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(' '))

def word_count(s):
    
    d = {}
    s = s.split()
    s = [''.join([char for char in word if char not in ignore]).lower() for word in s]
    s = [word for word in s if word != '' and word != ' ']
    
    for word in s:
        
        if word in d:
            
            d[word] += 1
        
        else:
            
            d[word] = 1
    
    return d


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    