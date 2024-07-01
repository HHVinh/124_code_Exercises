#Nhap so A tu ban phim va chuyen sang kieu so thuc
print('Nhập vào số cần làm tròn:')
soA = float(input())

#Nhap so B tu ban phim va chuyen sang kieu so nguyen
print('Nhập vào số lượng thập phân cần làm tròn:')
soB = int(input())

#Dung ham format de dinh dang chuoi dau ra
print('{0:.{1}f}'.format(soA, soB))