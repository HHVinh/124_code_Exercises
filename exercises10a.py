try:
    # Mở file 'bai10aVao.txt' để ghi dữ liệu
    with open('bai10aVao.txt', 'w') as fileInp:
        fileInp.write('Huynh Huu Vinh\n')  # Ghi tên vào file
        fileInp.write("27\n")  # Ghi tuổi vào file

    # Mở file 'bai10aVao.txt' để đọc dữ liệu
    with open('bai10aVao.txt', 'r') as fileInp:
        ten = fileInp.readline().strip()  # Đọc tên và loại bỏ ký tự xuống dòng
        tuoi = int(fileInp.readline().strip())  # Đọc tuổi, loại bỏ ký tự xuống dòng và chuyển thành số nguyên

    # Mở file 'bai10aRa.txt' để ghi kết quả
    with open('bai10aRa.txt', 'w') as fileOut:
        fileOut.write(f'Vao 20 nam nua tuoi cua {ten} se la {tuoi + 20}')  # Ghi kết quả vào file

# Khối lệnh xử lý lỗi khi không tìm thấy file đầu vào
except FileNotFoundError:
    with open('bai10aRa.txt', 'w') as fileOut:
        # Ghi thông báo lỗi vào file đầu ra
        fileOut.write('Khong tim thay file input!')

# Khối lệnh xử lý lỗi khi xảy ra lỗi khác (như lỗi định dạng đầu vào)
except Exception:
    with open('bai10aRa.txt', 'w') as fileOut:
        # Ghi thông báo lỗi vào file đầu ra
        fileOut.write('Dinh dang dau vao khong hop le!')
