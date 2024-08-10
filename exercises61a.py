def bien_Doi_Chuoi(s):
    if len(s) == 0:
        return 'Hãy nhập ít nhất 1 kí tự'
    elif s.startswith('*') and s.endswith('*'):
        return s.title()
    elif s.startswith('-') and s.endswith('-'):
        return s.swapcase()
    else:
        return s.capitalize()
    
s = input('Nhập một chuỗi bất kì: ')
print(bien_Doi_Chuoi(s))
    