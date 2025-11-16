a = "Hello Guy!"

def say():
    global a          
    a = "Vinh University"
    print("Trong hàm:", a)

say()
print("Ngoài hàm:", a)
