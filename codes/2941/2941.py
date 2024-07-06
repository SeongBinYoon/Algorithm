# 2941 크로아티아 알파벳

def croatia(word):
    dic = {'c=': 1, 'c-': 1, 'dz=': 2, 'd-': 1, 'lj': 2, 'nj': 2, 's=': 1, 'z=': 1}
    
    '''
    for s in word:
        if s not in dic:
            count += 1
        else:
            count += dic[s]
    '''
    return 0

x = input()
result = croatia(x)
print(result)