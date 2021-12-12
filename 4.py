a = int(input())
maxim = a % 10
a = a // 10
while a > 0:
    if a % 10 > maxim:
        maxim = a % 10
    a = a // 10
print(maxim)