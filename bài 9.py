string = input("Nhập vào một chuỗi: ")

d = {}  

for ch in string:       
    if ch in d:            
        d[ch] += 1         
    else:
        d[ch] = 1         

print("Kết quả đếm ký tự:", d)

