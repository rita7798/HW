#7. Спрашивает у пользователя число и выводит на экран все натуральные чётные числа,
# которые являются степенью двойки и не превышают введённого числа.
n = int(input("Введите число: "))
r = 1
t = 2**r
while t <= n:
    print (t)
    r+=1
    t = 2**r
  
