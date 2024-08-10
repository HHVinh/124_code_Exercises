def xu_Ly_Chuoi(s):
    if len(s) == 0:
        return 'Hãy nhập ít nhất 1 kí tự'
    for i in range(len(s)):
        if s[i].isalpha():
            break
    if s[i].islower() == True:
        return s.lower()
    return s.upper()

s = input('Nhập 1 chuỗi bất kì: ')
print(xu_Ly_Chuoi(s))
