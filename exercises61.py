def bien_doi_chuoi(s):
   if s.startswith('*') and s.endswith('*'):
       return s.title()
  
   if s.startswith('-') and s.endswith('-'):
       return s.swapcase()
      
   return s.capitalize()

#Nhap gia tri tu ban phim
s = input()

#Goi ham va truyen cac tham so can thiet
print(bien_doi_chuoi(s))
