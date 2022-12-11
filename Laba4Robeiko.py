""" Zadanie 1. Utwórz listę lista_zakupow zawierającą nazwy co najmniej czterech produktów spożywczych.
Następnie:
• wyświetl pierwszy i drugi element z listy
• zmień trzeci element listy na „mleko”
• wyświetl przedostatni i ostatni element listy

x = ["kiełbasa", "tomat", "ryż", "hleb"]
print(x[0])
print(x[1])

x[2] = "mleko"
print(x)

print(x[-2:])

"""
########################################################################################################################
""" Zadanie 2.
• Utwórz listę zestaw_1 zawierającą liczby losowe z przedziału [1, 10]. Liczbę elementów listy podaje
użytkownik. Wyświetl listę.
• Utwórz drugą listę zestaw_2 zawierającą liczby losowe z przedziału [5, 15]. Liczbę elementów listy
podaje użytkownik. Wyświetl listę.
• Pobierz od użytkownika liczbę. Napisz instrukcję warunkową, która na podstawie wartości
zapisanych w listach wyświetli jeden z poniższych komunikatów: „Liczba z zestawu 1”, „Liczba z
zestawu 2” albo „Nie ma takiej liczby w obu zestawach”.
• Utwórz listę zestaw_1_2 będącą złączeniem wartości z list zestaw_1 oraz zestaw_2. Posortuj i wyświetl
listę.

import random
u = int(input("podaj lichbe: "))
b = []
for i in range(u):
    x = random.randint(1, 10)
    b.append(x)
print(b)
u = int(input("podaj lichbe: "))
#b_2 = []
#for i in range(u):
 #   x = random.randint(5, 15)
 #   b_2.append(x)
b_2=[random.randint(5, 15) for i in range(u)]
print(b_2)
g = int(input('Podaj liczbe: '))
if g in b:
    print('Liczba z zastawu b')
elif g in b_2:
    print('Liczba z 2 ')
else:
    ('instrukcja')
b_3=b+b_2
print(b_3)
b_3.sort()
print(b_3)
"""
########################################################################################################################
"""Zadanie 5. Utwórz listę punkty będącą listą punktów zdobytych z pewnego egzaminu przez grupę 15 studentów.
Punkty niech będą liczbami rzeczywistymi z przedziału [0; 50]. Następnie
• Wyświetl informację o największej i najmniejszej ilości zdobytych punktów
• Wyświetl indeks pierwszego wystąpienia punktów podanych przez użytkownika. Jeżeli taka liczba
punktów nie występuje na liście, wyświetl odpowiedni komunikat
• Oblicz średnią punktów liczbę punktów z egzaminu
• Oblicz, ile osób zdobyło punkty powyżej, a ile poniżej średniej
• Wyświetl punkty poniżej średniej
• Wyświetl punkty powyżej średniej

import random
#punkty = []
#for i in range(15):
#    p = round(random.uniform(0, 50), 2)
#    #p = round(p, 2)
#    punkty.append(p)
punkty = [round(random.uniform(0, 50), 2) for i in range(15)]
print(punkty)
print(f"Maximum = {max(punkty)}, minimum = {min(punkty)}")

p=float(input('podaj liczbe '))
if p in punkty:
 x = punkty.index(p)
print(x)
else:
print('nie ma lizhbe v punlktu')
p = float(input("p "))
if p in grades:
    x = grades.index(p)
    print(x)
else:
    print("no")
sr = round(sum(grades)/len(grades), 2)
print(sr)
upper = []
lower = []
for i in grades:
    if i > sr:
        upper.append(i)
    elif i < sr:
        lower.append(i)
print(lower, upper)
print(len(lower), len(upper))
"""
########################################################################################################################
"""Zadanie 6.
• Załóżmy, że lista X składa się z 10 elementów. Przenieś ostatnie trzy elementy z końca na początek listy
bez zmiany ich oryginalnej kolejności.
• Utwórz listę Y, wykonując operację: Y = X. Następnie zmień jeden z elementów listy Y. Wyświetl obie listy
na ekranie.

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = []
y.insert(0, x[-3:])
y.append(x[:-3])
print(y, x)
"""
########################################################################################################################
"""Zadanie dodat.1. (Scal listy). Utwórz dwie listy liczb całkowitych. Następnie posortuj obie listy. Na wyjściu powinien
pojawić się jeden posortowany ciąg liczb scalony z tych dwóch list.

import random
a = int(input("podaj lichbe: "))
b = []
c = []
for i in range(a):
    x = random.randint(1, 50)
    b.append(x)

a = int(input("podaj lichbe: "))
b_2 = []
for i in range(a):
    x = random.randint(1, 60)
    b_2.append(x)

c = b+b_2
c.sort()
print(c)
"""
########################################################################################################################
"""Zadanie dodat.2. Zadeklaruj listę dwuwymiarową [n][2]. W programie umieść w tablicy odpowiednio: w kolumnie
pierwszej kolejne liczby całkowite, w kolumnie drugiej – kwadraty tych liczb. Wyświetl zawartość macierzy

x = [[3, 4, 5],
     []]
y = []
y = y + x[0]
y = [i**2 for i in y]
x[1] = y
print(x)
"""
########################################################################################################################
"""Zadanie dodat.3. Wypełnij listę dwuwymiarową na wzór szachownicy wartościami 0 i 1.

 a = [
     [0, 1, 0, 1, 0, 1],
     [1, 0, 1, 0, 1, 0],
     [0, 1, 0, 1, 0, 1],
     [1, 0, 1, 0, 1, 0],
     [0, 1, 0, 1, 0, 1],
     [1, 0, 1, 0, 1, 0]
     ]
 for i in a:
     print(i)
"""
