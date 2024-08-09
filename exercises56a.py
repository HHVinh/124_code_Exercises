def chuoi_Dao_Nguoc(s,a,b):
    catChuoi = s[a:b+1]
    daoNguoc = catChuoi[::-1]
    return daoNguoc

try:
    s = input('Nhập vào chuỗi ban đầu:')
    a,b = map(int,input('Nhập vào 2 kí tự bắt đầu và kết thúc của chuỗi con: ').split())

    if a < 0 or b < 0:
        print('Số nhập vào phải từ 0 trở lên')
    elif a > b:
        print('Số bắt đầu phải nhỏ hơn số kết thúc')
    elif b >= len(s):
        print('Số nhập vào lớn hơn độ dài chuỗi')
    else:
        print(chuoi_Dao_Nguoc(s,a,b))
except:
    print('Dữ liệu đầu vào không hợp lệ')
