def phep_Tinh(soThu1,phepTinh,soThu2):
    if phepTinh == '+':
        return soThu1 + soThu2
    elif phepTinh == '-':
        return soThu1 - soThu2
    elif phepTinh == '*':
        return soThu1 * soThu2
    elif phepTinh == ':' or phepTinh == '/':
        return soThu1 / soThu2
    else:
        print('Phép tính chưa đúng')

try:
    soThu1,phepTinh,soThu2 = input('Nhập phép toán muốn thực hiện: ').split()
    soThu1,soThu2 = map(float,[soThu1,soThu2])
    if (phepTinh == ':' or phepTinh == '/') and soThu2 == 0:
        print('Số bị chia phải khác 0')
    else:    
        print(f'Kết quả của {soThu1} {phepTinh} {soThu2} = {phep_Tinh(soThu1,phepTinh,soThu2)}')
except:
    print('Dữ liệu đầu vào không hợp lệ')
