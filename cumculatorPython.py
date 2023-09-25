import math
#сложенька(1)
def slogenie(a1, b1):
    return (a1 + b1)

#вычитанька(2)
def vichitanie(a2, b2):
    return(a2 - b2)

#умноженька(3)
def umnogenie(a3, b3):
    return(a3 * b3)

#деленька(4)
def delenie(a4, b4):
    if b4 == 0 :
        print("на ноль делить же нельзя!")
        return 1
    else : 
        return(a4 / b4)

#возведенька в степень(5)
def stepen(a5, b5):
    return(a5 ** b5)

#квадратный коренька(6)
def kvadratkoren(a6):
    return(a6 * (0.5))

#факториалик(7)
def factorial(a7): 
    if(a7==1 or a7==0): 
        return 1 
    else: 
        return a7*factorial(a7-1)
    
#синусик числа(8)
def sinus(a8):
    return(math.sin(a8))

#косинусик числа(9)
def cosinus(a9):
    return(math.cos(a9))

#тангенсик числа(10)
def tangens(a10):
    return(math.tan(a10))

d = True
while (d):
    print("В ЭТОМ КАЛЬКУЛЯТОРЕ ВЫ МОЖЕТЕ ВЫПОЛНИТЬ НЕСКОЛЬКО ДЕЙСТВИЙ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение числа в степень")
    print("6. Найти квадратный корень из числа")
    print("7. Найти факториал числа")
    print("8. Синус от числа")
    print("9. Косинус от числа")
    print("10. Тангенс от числа")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   

    while True:
        try:
           menu = int(input("Выберите действие которое выхотите выполнить: "))
           break
        except ValueError:
             print("Упси")

    if int(menu) == 1:
        while True:
             try:
                  result1 = slogenie(a1=int(input("Введите первое число: ")),
                       b1=int(input("Введите второе число:  ")))
                  print("сумма чисел равняется :", result1)
                  break
             except ValueError:
                  print("Упси")


    elif int(menu) == 2:
        while True:
             try: 
                  result2 = vichitanie(a2=int(input("Введите первое число: ")),
                              b2=int(input("Введите второе число: ")))
                  print("разность чисел равняется :", result2)
                  break
             except ValueError:
                  print("Упси")


    elif int(menu) == 3:
        while True:
             try: 
                  result3 = umnogenie(a3=int(input("Введите первое число: ")),
                                 b3=int(input("Введите второе число: ")))
                  print("произведение чисел равняется :", result3)
                  break
             except ValueError:
                  print("Упси")


    elif int(menu) == 4:
        while True:
             try:
                  result4 = delenie(a4=int(input("Введите первое число: ")),
                           b4=int(input("Введите второе число: ")))
                  print("деление чисел равняется :", result4)
                  break
             except ValueError:
                  print("Упси")
       

        
    elif int(menu) == 5:
         while True:
              try:
                   result5 = stepen(a5=int(input("Введите число: ")),
                          b5=int(input("Введие степень в которую хотите возвести число: ")))
                   print("число в степени равняется :", result5)
                   break
              except ValueError:
                  print("Упси")


    elif int(menu) == 6:
          while True:
               try:
                    result6 = kvadratkoren(a6=int(input("Введите число: ")))
                    print("корень равняется :", result6)
                    break
               except ValueError:
                  print("Упси")


    elif int(menu) == 7:
         while True:
               try:
                    result7 = factorial(a7=int(input("Введите число: ")))
                    print("факториал из числа равняется :", result7) 
                    break
               except ValueError:
                  print("Упси")


    elif int(menu) == 8:
        while True:
               try:
                    result8 = sinus(a8=int(input("Введите число: ")))
                    print("синус числа равняется :", result8) 
                    break
               except ValueError:
                  print("Упси")


    elif int(menu) == 9:
        while True:
               try:
                    result9 = cosinus(a9=int(input("Введите число: ")))
                    print("косинус числа равняется :", result9)
                    break
               except ValueError:
                  print("Упси")


    elif int(menu) == 10:
        while True:
               try:
                    result10 = tangens(a10=int(input("Введите число: ")))
                    print("тангенс числа равняется :", result10) 
                    break
               except ValueError:
                  print("Упси")

    
    elif int(menu) < 1 or int(menu) > 10:
        print("Так нельзя, вы чево")
    

    go_again = input("Хотите продолжить выполнять действия? (да или нет)")
    if go_again == "нет":
        break

