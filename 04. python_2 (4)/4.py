#4.Спрашивает у пользователя число N, а затем N раз спрашивает у пользователя слово  и выводит его на экран.
#Если пользователь ввел слово "программирование", программа должна завершить работу.
n = int(input("Введите число: "))
for n in range(0, n) :
    s = input("Введите слово: ")
    if s == "программирование":
        break
    print (s)
