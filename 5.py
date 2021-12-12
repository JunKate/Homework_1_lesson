# a - выручка
# b - издержки
#
# =>>??? a >< b
#
# if a > b - True => babki = a- b =>> pp(?) =>> babki / pp
#     b > a => break

a = int(input("Введите выручку: "))
b = int(input("Введите издержки: "))

if a > b:
    lave = (a - b)
    ppl_work = int(input("Введите кол-во сотрудников:  "))
    x = float(lave / ppl_work)
    print((f"Мы получили прибыль {lave:.1f}, каждый сотрудник получит {x} денег!"))

else:
    print("Денег нет, но вы держитесь")
