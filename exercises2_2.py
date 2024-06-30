# Nếu muốn người dùng nhập lại sau khi nhập sai chatGPT hướng dẫn
def nhap_so_nguyen(thong_bao): # Định nghĩa hàm nhap_so_nguyen với tham số thong_bao
    while True: # Bắt đầu vòng lặp vô hạn để yêu cầu nhập lại nếu xảy ra lỗi
        try: # Bắt đầu khối try để kiểm tra lỗi
            return int(input(thong_bao)) # Yêu cầu người dùng nhập vào giá trị, chuyển đổi thành số nguyên và trả về giá trị đó
        except ValueError: # Nếu xảy ra lỗi ValueError (người dùng nhập không phải là số nguyên)
            print("Vui lòng nhập một số nguyên hợp lệ.") # In ra thông báo lỗi và tiếp tục vòng lặp yêu cầu nhập lại


a = nhap_so_nguyen('Nhập số thứ 1: ')
b = nhap_so_nguyen('Nhập số thứ 2: ')
tong = a + b
print('Tổng hai số nguyên là:', tong)