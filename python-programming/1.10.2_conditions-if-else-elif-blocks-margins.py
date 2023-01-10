n = int(input())
if  1900 > n > 3000:
    print ('Ошибка')
elif (n % 4) == 0 and (n % 100):
    print ('Високосный')
elif (n % 400) == 0:
    print ('Високосный')
else:
    print ('Обычный')