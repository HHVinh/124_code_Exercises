def danh_Sach_Hai_Chieu(M,N):
    danhSach =[]
    for i in range(M):
        while True:
            hang = input(f'Hãy nhập dữ liệu của hàng {i+1} với {N} giá trị: ').split()
            if len(hang) == N:
                danhSach.append(hang)
                break       
            else:
                print('Số cột chưa đúng')
    return danhSach

M, N = map(int,input('Hãy nhập 2 số hàng và cột cách nhau bởi dấu cách: ').split())

ketQua = danh_Sach_Hai_Chieu(M,N)
print('Danh sách hai chiều: ',)
for hang in ketQua:
    print(' '.join( hang))

    