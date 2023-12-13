def power(base, exponent):
    return base ** exponent if exponent >= 0 else "Степінь має бути не від'ємним числом"

base = 2
exponent = 3
result = power(base, exponent)
print(result)
