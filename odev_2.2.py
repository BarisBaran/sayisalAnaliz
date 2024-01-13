def f(x):
    return x**3 + 4*x**2 - 10

def bisection_method(a, b, epsilon):
    iter_count = 0
    
    while (b - a) / 2 > epsilon:
        mid = (a + b) / 2
        if f(mid) == 0:
            return mid  # Kök bulundu
        elif f(mid) * f(a) < 0:
            b = mid
        else:
            a = mid
        iter_count += 1
    
    return (a + b) / 2

# Başlangıç aralığı
a = 1
b = 2

# Bağıl hata payı
epsilon = 10**-6 * (b - a) / 2

# İkiye bölme yöntemi uygula
result = bisection_method(a, b, epsilon)

print("Bulunan kök:", result)
