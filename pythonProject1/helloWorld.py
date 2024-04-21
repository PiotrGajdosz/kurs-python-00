
import hello
import triangle_cnt
import avg_spd
from calculations.money_deposit import *


liczba = 10
print(liczba)
dictionary = {
    "prad": 250,
    "woda": 500,
    "zakupy": ["jajka", "maslo", "chleb"]
}
print(dictionary)

int_val = 30
print('int value:\t ', int_val, '\t Typ: ', type(int_val), sep='\t\t')
print('int value:\t ', int_val, '\t Typ: ', type(int_val))
print('int value:', int_val, ' Typ: ', type(int_val))


number = 1
while number % 2 != 0:
    number = int(input("Podaj licze parzysta: "))
print("Brawo")

lista = ["chleb", "woda", "jajka", "maslo", "dzem"]

# wypisanie elementow z indeksem
for index, poz in enumerate(lista):
    print(index, poz)

# wypisanie elementow slownika na zasadzie klucz-wartosc
for dictionary_name, dictionary_value in dictionary.items():
    print(dictionary_name, dictionary_value)

# wypisanie liter ze stringa
my_string = "string_for_test"
for letter in my_string:
    print(letter)

podatki = [100, 200, 300, 400, 500, 600]
for podatek in podatki:
    print(podatek)


def get_best_grade(grades):
    avg_grades = []
    for grades_sub, grades_value in grades.items():
        avg_grades.append(sum(grades_value) / len(grades_value))
    return avg_grades


grades_data = {
    "Art": [3, 4, 3, 4],
    "Math": [15, 3, 2, 4],
    "PE": [4, 42, 4, 3]
}
print("srednie ocen to: ")
print(get_best_grade(grades_data))

hello.say_hello()
hello.say_hello_with_name("Piotr")

droga = int(input("Podaj dystans: "))
czas = int(input("Podaj czas"))
print("Predkosc wynosi: ", avg_spd.get_avg_spd(droga, czas))


len_1 = int(input("Podaj dlugosc przyprostokatnej 1: "))
len_2 = int(input("Podaj dlugosc przyprostokatnej 2: "))
print("Dlugosc przeciwprostokatnej wynosi: ", triangle_cnt.get_triangle_length(len_1, len_2))


money = float(input("Podaj kwote do wpłacenia: "))
depo_time = float(input("Podaj czas lokaty w latach: "))
perc = float(input("Podaj oprocentowanie lokaty w skali roku: "))
print("Wartosc lokaty wynosi: ", get_depo_profit(money, depo_time, perc))


