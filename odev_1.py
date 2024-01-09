import math

def cos_taylor(x, n):
    result = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
        result += term
    return result

# π/5 noktasındaki değeri hesapla
x_value = math.pi / 5
degree = 10  # İstenilen dereceyi belirtin, örneğin 10
cos_approximation = cos_taylor(x_value, degree)

print(f"cos({x_value}) yaklaşık değeri: {cos_approximation}")
