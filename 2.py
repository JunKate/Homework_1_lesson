# 3600 сек  - 1 час
# 60 сек - 1 минута
# Используйте форматирование строк.
# чч:мм:сс


uno = 3600

a = int(input("Введите время в секундах "))
hours = (a // uno)
minutes = (a - (hours * uno)) // 60
sek = a - (hours * uno) - (minutes * 60)

# print("%d:%d:%d" % (hours, minutes, sek))

print(f"{hours:02d}:{minutes:02d}:{sek:02d}")    # спасибо гугл, что ты есть <3

