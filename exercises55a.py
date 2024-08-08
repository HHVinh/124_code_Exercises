def kiem_Tra_Chuoi(s1, s2):
    if s2 in s1:
        print('{} xuất hiện {} lần trong {}'.format(s2,s1.count(s2),s1))
    return f'{s2} không tồn tại trong {s1}'

s1 = input('Nhập chuỗi thứ nhất: ')
s2 = input('Nhập chuỗi thứ hai: ')

kiem_Tra_Chuoi(s1,s2)
