def giaTri_Soluong_Vitri(s):
    a = max(s)
    b = s.count(a)
    c = [i for i, x in enumerate(s) if x == a]
    return a, b, c

s = input('Nhập dãy số bất kì: ').split()
if len(s) == 0:
    print('Dữ liệu rỗng')
else:    
    try:
        danhSach = list(map(int,s))
        a, b, c = giaTri_Soluong_Vitri(danhSach)
        print(f'Số lớn nhất là: {a}')
        print(f'Số lần lặp lại của {a} là {b} lần')
        print(f'Các vị trí của {a} trong dãy vừa nhập là: ',*c)
    except:
        print('Dữ liệu đầu vào chưa hợp lệ')
