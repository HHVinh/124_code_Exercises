def dem_0(n):
    soPhanTu0 = tuple(n).count('0')
    soKytu0 = [ptu.count('0') for ptu in n]
    return soPhanTu0, sum(soKytu0)

n = tuple(input('Nhập các giá trị bất kì: ').split())
dem0 = dem_0(n)
print(dem0)