def so_Lan_Xuat_Hien(s):
    setA = set(s)
    for i in setA:
        dem = s.count(i)
        print(f"Ký tự: {i}, Số lần xuất hiện: {dem}")

s = input('Nhập dữ liệu bất kì: ')
so_Lan_Xuat_Hien(s)

    