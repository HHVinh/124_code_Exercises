def tong_Ptu(tupleX):
    # Tính tổng các phần tử trong từng tuple con
    tong = tuple(sum(ptu) for ptu in tupleX)
    return tong

try:
    n = int(input('Nhập một số tự nhiên bất kì: '))
    if n < 0:
        print('Hãy nhập một số nguyên dương!')
    else:
        ketQua = []
        for i in range(n):
            duLieuVao = input(f'Hãy nhập dữ liệu hàng thứ {i+1}: ')
            try:
                # Chuyển dữ liệu thành tuple số nguyên
                tupleCon = tuple(map(int, duLieuVao.split()))
                ketQua.append(tupleCon)
            except ValueError:
                print('Hãy nhập các số tự nhiên bất kì!')
                break
        if len(ketQua) == n:
            # In danh sách tuple con
            ketQua = tuple(ketQua)
            print("Các tuple con:", ketQua)

            # Tính tổng các phần tử trong từng tuple con
            tongCong = tong_Ptu(ketQua)
            print("Tổng các phần tử trong từng tuple con:", tongCong)
except ValueError:
    print('Dữ liệu đầu vào không hợp lệ!')
