# Nhập dãy số từ người dùng
daySo = input('Nhập các số muốn tính tổng, cách nhau bởi khoảng trắng: ')
        
# Chia chuỗi thành các phần tử
chuyenThanhChuoiCon = daySo.split()
while True:
    try:        
        # Chuyển đổi các phần tử thành số nguyên
        chuyenThanhSoNguyen = map(int, chuyenThanhChuoiCon)
        
        # Tính tổng và in kết quả
        tong = sum(chuyenThanhSoNguyen)
        print('Tổng dãy số là:', tong)
        
        # Thoát khỏi vòng lặp khi mọi thứ đã thành công
        break
    except ValueError:
        # Xử lý lỗi nếu dữ liệu nhập không thể chuyển thành số nguyên
        print('Dữ liệu nhập vào không hợp lệ. Vui lòng nhập lại dãy số chỉ chứa các số nguyên.')
