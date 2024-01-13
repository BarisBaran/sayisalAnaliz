def f(x):
    return x**3

def ileriFarkYöntemi(x, h):
    return (f(x + h) - f(x)) / h

def geriFarkYöntemi(x, h):
    return (f(x) - f(x - h)) / h

def merkeziFarkYöntemi(x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# x = 1 noktasındaki türevi h=0.2 ve h=0.1 kullanarak hesapla
x = 1
h1 = 0.2
h2 = 0.1

beklenenDeger = 3  # x=1 noktasındaki beklenen türev değeri

ileriFarkHesaplanan_h1 = ileriFarkYöntemi(x, h1)
geriFarkHesaplanan_h1 = geriFarkYöntemi(x, h1)
merkeziFarkHesaplanan_h1 = merkeziFarkYöntemi(x, h1)

ileriFarkHesaplanan_h2 = ileriFarkYöntemi(x, h2)
geriFarkHesaplanan_h2 = geriFarkYöntemi(x, h2)
merkeziFarkHesaplanan_h2 = merkeziFarkYöntemi(x, h2)

print("Beklenen Türev Değeri (x=1):", beklenenDeger)
print("\nAdım H = 0.2 için:")
print("İleri Fark Yöntemi ile Hesaplanan Türev:", ileriFarkHesaplanan_h1)
print("Geri Fark Yöntemi ile Hesaplanan Türev:", geriFarkHesaplanan_h1)
print("Merkezi Fark Yöntemi ile Hesaplanan Türev:", merkeziFarkHesaplanan_h1)

print("\nAdım H = 0.1 için:")
print("İleri Fark Yöntemi ile Hesaplanan Türev:", ileriFarkHesaplanan_h2)
print("Geri Fark Yöntemi ile Hesaplanan Türev:", geriFarkHesaplanan_h2)
print("Merkezi Fark Yöntemi ile Hesaplanan Türev:", merkeziFarkHesaplanan_h2)
