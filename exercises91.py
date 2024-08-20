def danh_Sach_Hai_Chieu(M, N):
    danhSach = []
    for i in range(M):
        while True:
            # Nhập dữ liệu cho từng hàng và tách thành danh sách các giá trị
            hang = input(f'Hãy nhập dữ liệu của hàng {i+1} với {N} giá trị (các giá trị cách nhau bằng dấu cách): ').split()
            
            # Kiểm tra số lượng phần tử của hàng
            if len(hang) == N:
                danhSach.append(hang)
                break
            else:
                print(f'Số cột chưa đúng. Vui lòng nhập đúng {N} giá trị.')
    return danhSach

# Nhập kích thước của danh sách hai chiều
M, N = map(int, input('Hãy nhập số hàng và số cột cách nhau bởi dấu cách: ').split())

# Gọi hàm để nhập và lưu danh sách hai chiều
ketQua = danh_Sach_Hai_Chieu(M, N)

# Hiển thị kết quả
print('Danh sách hai chiều:')
for hang in ketQua:
    print(' '.join(hang))
