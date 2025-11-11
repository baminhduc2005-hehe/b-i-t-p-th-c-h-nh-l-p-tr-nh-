import math

# Nhập tọa độ điểm thứ nhất
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

# Nhập tọa độ điểm thứ hai
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Tính khoảng cách theo công thức √((x2-x1)^2 + (y2-y1)^2)
dx = (x2 - x1) ** 2
dy = (y2 - y1) ** 2
distance = math.sqrt(dx + dy)

# In kết quả
print("Distance between two points:", round(distance, 2))
