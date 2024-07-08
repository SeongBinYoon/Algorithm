# 2941 크로아티아 알파벳

def croatia(word):
    arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    for s in arr:
        word = word.replace(s, '0')
    
    return len(word)

x = input()
result = croatia(x)
print(result)