def f(x):
    return x**3 - 2*x**2 - 5

def bisection_method(a, b, tol, max_iter):
    iter_count = 0
    
    while (b - a) / 2 > tol and iter_count < max_iter:
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
a = 2
b = 4

# Tolerans ve maksimum iterasyon sayısı
tolerance = 1e-5
max_iterations = 4

# İkiye bölme yöntemi uygula
result = bisection_method(a, b, tolerance, max_iterations)

print("Bulunan kök:", result)
