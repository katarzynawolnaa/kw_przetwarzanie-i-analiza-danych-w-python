# -*- coding: utf-8 -*-
"""Zadania-30-10-2023.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EKGKWyuMOb0IZt550kIoAztGygILCFl9

Zad.1
"""


def wyswietl_imiona(imiona):
    if len(imiona) != 5:
        print("Proszę podać dokładnie 5 imion.")
    else:
        for imie in imiona:
            print(imie)


lista_imion = list(str)["Kasia", "Julia", "Dominika", "Tomasz", "Michal"]
wyswietl_imiona(lista_imion)

"""Zad.2"""

# Wykorzystując petle for


def pomnoz_przez_dwa_for(lista_liczb):
    wynik = []
    for liczba in lista_liczb:
        wynik.append(liczba * 2)
    return wynik


lista = [1, 2, 3, 4, 5]
wynik = pomnoz_przez_dwa_for(lista)
print(wynik)

# Wykorzystujac liste składana


def pomnoz_przez_dwa_lista_skladana(lista_liczb):
    return [liczba * 2 for liczba in lista_liczb]


lista = list(int)[1, 2, 3, 4, 5]
wynik = pomnoz_przez_dwa_lista_skladana(lista)
print(wynik)

"""Zad.3"""


def wyswietl_parzyste_elementy(lista_liczb):
    for liczba in lista_liczb:
        if liczba % 2 == 0:
            print(liczba)


lista = list(range(1, 11))
wyswietl_parzyste_elementy(lista)

"""Zad.4"""


def wyswietl_co_drugi_element(lista_liczb):
    for i in range(0, len(lista_liczb), 2):
        print(lista_liczb[i])


lista = list(range(1, 11))
wyswietl_co_drugi_element(lista)
