import math

def f(x):
    return 4 * math.exp(-0.5 * x) - x

def df(x):
    return -2 * math.exp(-0.5 * x) - 1

def newton_raphson_method(x0, max_iter):
    iter_count = 0
    x = x0
    
    while iter_count < max_iter:
        x = x - f(x) / df(x)
        iter_count += 1
    
    return x

# Başlangıç değeri
x0 = 2

# Maksimum iterasyon sayısı
max_iterations = 4

# Newton-Raphson yöntemi uygula
result = newton_raphson_method(x0, max_iterations)

print("Bulunan kök:", result)
