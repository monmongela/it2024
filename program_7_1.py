d = int(input())
x = int(input())
a = (365 - (75) / (d * d * d)) / (3 * d * d - d) * 5
b = (412 - (125) / (d * d * d)) / (2 * d * d - d) * 4
a1 = a * d * x
b1 = b * d * x
n = ((a1 + b1) / 3)
n1 = round(n)
print(n1)
