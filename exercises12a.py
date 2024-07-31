try:
    # Mở file 'bai12aVao.txt' để ghi dữ liệu
    with open('bai12aVao.txt', 'w') as fileInp:
        fileInp.write('Anh\n')
        fileInp.write('Vinh\n')
        fileInp.write('dep\n')
        fileInp.write('trai\n')

    # Mở file 'bai12aVao.txt' để đọc dữ liệu
    with open('bai12aVao.txt', 'r') as fileInp:
        fullFile = fileInp.read()  # Đọc toàn bộ nội dung file
        danhSachCacDong = fullFile.splitlines()  # Tách các dòng
        cauHoanChinh = ' '.join(danhSachCacDong)  # Kết hợp các dòng thành một chuỗi

    # Mở file 'bai12aRa.txt' để ghi kết quả
    with open('bai12aRa.txt', 'w') as fileOut:
        fileOut.write(cauHoanChinh)  # Ghi kết quả vào file

except FileNotFoundError:
    # Xử lý lỗi khi không tìm thấy file (không cần thiết ở đây vì ta đang mở file 'bai12aVao.txt' để ghi và đọc)
    with open('bai12aRa.txt', 'w') as fileOut:
        fileOut.write('Khong tim thay file input')

except Exception:
    # Xử lý lỗi khác (như lỗi định dạng dữ liệu)
    with open('bai12aRa.txt', 'w') as fileOut:
        fileOut.write('Du lieu dau vao khong hop le')
