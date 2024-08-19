
def so_Nguyen_To(n):
    if n <= 1:
        return False
    for i in range (2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def ds_So_Nguyen_To(danhSachSo):
    dsSoNguyenTo = [i for i in danhSachSo if so_Nguyen_To(i)]
    return dsSoNguyenTo

danhSach = input('Nhập các số tự nhiên bất kì: ').split()
if len(danhSach) == 0:
    print('Hãy nhập ít nhất một số bất kì')
else:
    try:
        danhSachSo = list(map(int, danhSach))
        dsSoNguyenTo = ds_So_Nguyen_To(danhSachSo)
        print(*dsSoNguyenTo)
    except:
        print('Dữ liệu đầu vào không hợp lệ')