# Chương trình máy tính thực hiện các phép tính đơn giản

# Hàm cộng hai số
def add(x, y):
    return x + y

# Hàm trừ hai số
def subtract(x, y):
    return x - y

# Hàm nhân hai số
def multiply(x, y):
    return x * y

# Hàm chia hai số
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Không thể chia cho 0!"

# --- Phần chương trình chính ---
print("Chọn phép tính:")
print("1. Cộng")
print("2. Trừ")
print("3. Nhân")
print("4. Chia")

# Người dùng chọn phép tính
choice = input("Nhập lựa chọn (1/2/3/4): ")

# Nhập hai số từ bàn phím
num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))

# Kiểm tra lựa chọn và gọi hàm tương ứng
if choice == '1':
    print("Kết quả:", add(num1, num2))
elif choice == '2':
    print("Kết quả:", subtract(num1, num2))
elif choice == '3':
    print("Kết quả:", multiply(num1, num2))
elif choice == '4':
    print("Kết quả:", divide(num1, num2))
else:
    print("Lựa chọn không hợp lệ!")
