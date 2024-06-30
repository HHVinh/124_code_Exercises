# Nếu trong code có thể xảy ra lỗi thì đưa vào giữa TRY và EXCEPT để thông báo lỗi
try:
    print('Nhập số thứ 1:')
    a = int(input())
    print('Nhập số thứ 2:')
    b = int(input())
    tong = a + b
    print('Tổng hai số nguyên là:', tong)
except:
    print('Bạn cần nhập số nguyên')


