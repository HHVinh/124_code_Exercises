#Khoi lenh co the phat sinh loi
try:
    #Nhap gia tri tu ban phim
    #Ep kieu du lieu sang so nguyen
    x = float(input("Nhập giá trị x: "))
    n = int(input("Nhập giá trị n: "))

    # Sử dụng cấu trúc rẽ nhánh xử lý trường hợp n < 0
    if n < 0:
        print("Vui lòng nhập n là số tự nhiên!")
    elif n == 0:
        print(1)
    else:
        ketQua = 1
        giaiThua = 1
        # Sử dụng vòng lặp for duyệt các số từ 1 tới 2*n
        for i in range(1, 2 * n + 1):
            giaiThua *= i
            if i % 2 == 0:
                ketQua += pow(x, i) / giaiThua
            else:
                ketQua -= pow(x, i) / giaiThua 
        print(f"Kết quả là: {ketQua:.5f}")

        
#Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")