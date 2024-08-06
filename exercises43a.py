def tenBanCaoHon(ten1,chieuCao1,ten2,chieuCao2):
    if chieuCao1 > chieuCao2:
        return ten1
    return ten2
try:
    ten1, chieuCao1 = input('Nhập tên và tuổi của bạn thứ nhất cách nhau bởi khoảng trắng: ').split()
    ten2, chieuCao2 = input('Nhập tên và tuổi của bạn thứ hai cách nhau bởi khoảng trắng: ').split()
    chieuCao1,chieuCao2 = map(int,(chieuCao1,chieuCao2))
    
    if chieuCao1 < 0 or chieuCao2 <0:
        print('Chiều cao phải lớn hơn 0')
    elif chieuCao1 == chieuCao2:
        print('Chiều cao hai bạn bằng nhau')
    else:
        banCaoHon = tenBanCaoHon(ten1,chieuCao1,ten2,chieuCao2)
        print(f'Bạn {banCaoHon} cao hơn')
except:
    print('Dữ liệu đầu vào không hợp lệ')
