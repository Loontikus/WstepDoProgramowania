#x = int (input("podaj lichbe:"))
#print(x,type(x))#
#x=1 + 2
'''print(x,type(x))
x=1 + 4.5
print(x,type(x))
x=3 / 2
print(x,type(x))
x=4 / 2
print(x,type(x))
x=3 // 2
print(x,type(x))
x=-3 // 2
print(x,type(x))
x=11.5 % 2
print(x,type(x))
x=2 ** 10
print(x,type(x))
x=8 ** (1/3)
print(x,type(x))


#2##################################
int(3.0)
x=1+2
print(x,type(x))
float(3)
x=1.0+2.0
print(x,type(x))
float("3")
str(12.4)#String?
x=str("12.4 ")
print(x,type(x))
bool(0)
x=bool(0)
print(x,type(x))'''
#Domowe1.1###############################
'''a=float(input("Liczbę"))
b=float(input("Liczbe"))
S=a*b
P=2*(a+b)
pole=f'Pole {S}'
obwód=f'Obwód {P}'
print(pole,obwód)'''
############################################################################################################
"""Zadanie #2 (2.py) Napisz skrypt, który pobiera od użytkownika drogę pokonaną przez samochód oraz średnie
spalanie (w litrach na 100 km) i wyświetli informację o przewidywanym zużyciu paliwa oraz o szacowanych
kosztach podróży (cena paliwa 6.5 zł/l).

x = int(input("input length: "))
y = int(input("average consumption: "))
#f = fuel consupmtion
#c = cost per trip
f = x*y/100
c = f*6.5
print("your fuel consumtion =", f,"cost of travel =", c)

"""
#3######################################################################
""""Zadanie 3 (3.py):
• Dla osób poniżej 4 roku życia wstęp jest bezpłatny.
• Dla osób w wieku od 4 do 18 lat bilet kosztuje 10zł.
• Dla osób powyżej 18 roku życia bilet kosztuje 20zł.
Przykład: Wprowadź wiek klienta: 5
Cena biletu: 10zł"""################################

'''x=int(input("Years: "))
if x<4:
    print("wstęp jest bezpłatny.")
elif x>=4 and x<=18:
    print("bilet kosztuje 10zł.")
else :
    print("bilet kosztuje 20zł.")'''#########################
#4######################################################################
"""x = str(input("enter letter: "))
if str.isupper(x):
    print("Upper")
if str.islower(x):
    print("Lower")"""""

#5################################################################################
"""print('''Jaką operację chcesz wykonać?
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie''')
d = int(input('Wpisz numer operacji: '))  # 4
a1 = float(input('Wpisz numer operacji: '))
a2 = float(input('Wpisz numer operacji: '))

if d == 1:
    w = a1 + a2
elif d == 2:
    w = a1 - a2
elif d == 3:
    w = a1 * a2
elif d == 4:
    w = a1 / a2
elif d == 5:
    w = a1 ** a2
else: print('błędna operacja')

print(f'wynik = {w}')"""
print('''Jaką operację chcesz wykonać?
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie''')
d = int(input('Wpisz numer operacji: '))  # 4
a1 = float(input('Wpisz argument1: '))
a2 = float(input('Wpisz argument2: '))

if d == 1:
    w = a1 + a2
elif d == 2:
    w = a1 - a2
elif d == 3:
    w = a1 * a2
elif d == 4:
    if a2 == 0:
        print('nie możemy dzielić przez zero')
        exit()
    else:
        w = a1 / a2
elif d == 5:
    w = a1 ** a2
else:
    print('błędna operacja')
    exit()

print(f'wynik = {w}')
