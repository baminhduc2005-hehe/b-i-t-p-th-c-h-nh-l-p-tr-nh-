a, b = 1, 2      
a, b = 1, 2     
total = 0       

print("Dãy Fibonacci nhỏ hơn 4.000.000 là:")

while a < 4000000:   
    print(a, end=" ")  
    if a % 2 == 0:     
        total += a   
    a, b = b, a + b
    print("\nTổng các số chẵn trong dãy Fibonacci là:", total)

