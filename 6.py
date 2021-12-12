a = int(input("Пробежка в первый день: "))
b = int(input("Пробежка в последний день: "))
num = a
while num <= b:
    num += 0.1*num
num = int(num)
print(f"На {num} день спортсмен достиг результата - не менее {b} км.")




