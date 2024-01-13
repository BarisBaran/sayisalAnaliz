import math

def f(x):
    return math.exp(x)

def ileriFarkYöntemi(x, h):
    return (f(x + h) - f(x)) / h

def geriFarkYöntemi(x, h):
    return (f(x) - f(x - h)) / h

def merkeziiFarkYöntemi(x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# x = 1 noktasındaki türevi h=0.2 kullanarak hesapla
x = 1
h = 0.2

expected_derivative = math.exp(1)

forward_result = forward_difference(x, h)
backward_result = backward_difference(x, h)
central_result = central_difference(x, h)

print("Beklenen Türev Değeri (e):", expected_derivative)
print("İleri Fark Yöntemi ile Hesaplanan Türev:", ileriFarkYöntemi)
print("Geri Fark Yöntemi ile Hesaplanan Türev:",geriFarkYöntemi)
print("Merkezi Fark Yöntemi ile Hesaplanan Türev:", merkeziFarkYöntemi)
