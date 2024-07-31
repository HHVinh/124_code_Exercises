while True:
    try:
        a = int(input('Nhập số nguyên bất kì: '))
        break
    except:
        print('Hãy nhập số nguyên')
print('Số thập phân %d trong hệ bát phân là %o '%(a,a))
