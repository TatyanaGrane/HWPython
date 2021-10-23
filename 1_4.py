# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

x = int(input("Enter number: "))
a = x % 10
while x > 0:
    if x % 10 > a:
        a = x % 10
    x = x // 10
print(a)

# из урока
#n = int(input())
#greatest = 0 # для хранения максимума
#num = n
#while num > 0:
 #   digit = num % 10
  #  if digit > greatest:
   #     greatest = digit
    #    if greatest == 9:
     #       break
    #num = num // 10
#print(f"Наиб цифра в числе {n} равна {greatest}")