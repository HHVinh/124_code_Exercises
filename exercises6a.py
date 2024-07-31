while True:
    try:
        a = float(input('Nhập số thập phân bất kì: '))
        b = int(input('Nhập số nguyên - là số lượng thập phân cần làm tròn: '))
        break
    except:
        print('Cần nhập đúng 2 số a và b')
print('Kết quả là: 'f'{a:.{b}f}')
