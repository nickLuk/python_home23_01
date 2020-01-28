import random
number = int(input("Enter number list "))
lista = []
for a in range(0,number):
    lista.append(random.randint(0,99)) # заповнюємо випадковими числами
print(lista)
j = 0
for i in range(int(len(lista)/2)):
    lista[j], lista[j+1] = lista[j+1], lista[j] # міняємо місцями сусідні елементи списку попарно
    j += 2
print(lista)
res = input("Бажаєте зберегти дані у файл - натисніть y, або n щоб вийти з програми\n")
if res == "y":
    with open("task3.txt", "w") as file:
        print(lista, file=file)
