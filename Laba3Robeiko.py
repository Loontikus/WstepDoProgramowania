"""Zadanie 1 (1.py) Napisz skrypt, który pobierze od użytkownika dwie liczby całkowite. Następnie zaczynając od
mniejszej liczby, wypisze kolejne liczby aż do osiągnięcia wartości drugiej (większej) liczby.
x = int(input("x= "))
y = int(input("y= "))
for n in range(x, y, 1):
    print(n)
if x > y:
    for n in range(y, x, 1):
        print(n) """
########################################################################################################################
"""Zadanie 2 (2.py) Napisz program, który wyświetli wartości funkcji 𝑦 = 2𝑥
2 − 5𝑥 − 8, dla 𝑥 ∈ [−4, 4], z krokiem
0.5.

solutions_string = ""
current_number = -4
while current_number <= 4:
    solutions_string += f"f({current_number}) = {2 * current_number ** 2-5 * current_number -8}\n"
    current_number += 0.5
print(solutions_string)
    """
########################################################################################################################
"""Zadanie 3 (3.py) Napisz pętlę nieskończoną, w której użytkownik podaje liczby całkowite. W przypadku liczby
ujemnej, następuję wyjście z pętli. 

a = int(input("Liczbe: "))
while a != 0:
    if a < 0:
        print("ujemna liczbe: ", a)
        break
    a = int(input())
else:
    print("oczekiwanie na liczbę ujemną ")
"""
########################################################################################################################
"""Zadanie 4 (4.py) Zmodyfikuj program z zad. 1 tak, aby przechodząc po kolejnych liczbach przedziału, wypisywać
tylko liczby parzyste, a nieparzyste – pomijać. Użyj instrukcji continue.

x = int(input("x= "))
y = int(input("y= "))

for n in range(x, y, 1):
    if n % 2 == 1:
        continue
    print(n)
if x > y:
    for n in range(y, x, 1):
        if n % 2 == 1:
            continue
        print(n)
"""
########################################################################################################################
"""Zadanie 5 (5.py) Grupa laboratoryjna składa się z n studentów (wartość n podaje użytkownik). Wprowadzamy
liczbę punktów dla każdego studenta. Napisz program, który obliczy średnią liczbę punktów w grupie z
wykorzystaniem pętli while.
n = int(input('how many students in the class? '))
i = 1
suma = 0
while i <= n:
    x = int(input(f'podai licb{i}: '))
    if x<0 or x>100:continue
    i += 1
    suma = suma + x
sred = suma/n
print(sred)

"""
########################################################################################################################
"""Zadanie 7 (7.py) Za pomocą pętli for wypisz na ekranie ciągi liczb:
• 1, 2, 3, ... , 99, 100
• 100, 99, ... , 2, 1, 0
• 7, 14, 21, ... , 70, 77
• 20, 18, ... , 2, 0

for i in range(0, 101):
    print(i, end = " ")
print()
for x in reversed(range(0, 101)):
    print(x, end = " ")
print()
for l in range(0, 85, 7):
    print(l, end = " ")
print()
for j in reversed(range(0, 22, 2)):
    print(j, end = " ")
"""
########################################################################################################################
"""
Zadanie 8 (8.py) Napisz skrypt, który wyświetli gwiazdki jak poniżej. Liczba wierszy (lub gwiazdek w linii)
powinna być podawana przez użytkownika.
Przykład: 3
* * *
* * *
* * *

x = int(input("Numer "))
for i in range(x):
    print("*"*x)
"""
########################################################################################################################
"""Zadanie 9 (9.py) Napisz program, który wyświetli „choinkę” jak poniżej. Wysokość „choinki” powinna być
podawana z klawiatury.

x = int(input("Number "))
for i in range(x+1):
    print(" "*(x-i)+"* "*i)

"""
