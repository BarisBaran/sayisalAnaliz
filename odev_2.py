https://drive.google.com/drive/folders/1bl2O-rT7k__Zvi_Esh4MWssECK7cBkvI
sayısal analiz çdev linki 
def f(x):
    return x**3 - 2*x**2 - 5

def bisection_method(a, b, tol, max_iter):
    if f(a) * f(b) > 0:
        print("Bu aralıkta bir kök yok.")
        return None
    
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1

    return (a + b) / 2

# Başlangıç aralığı [2, 4]
a = 2
b = 4

# Tolerans ve maksimum iterasyon sayısı
tolerance = 1e-6
max_iterations = 4

# İkiye bölme metodu ile kökü hesapla
result = bisection_method(a, b, tolerance, max_iterations)

if result is not None:
    print(f"{max_iterations} iterasyonda bulunan kök: {result}")
else:
    print("İtere bölme metodu başarısız oldu.")
