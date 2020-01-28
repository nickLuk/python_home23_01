lista = [55, 56, 10, 25, 555, 28, 289, 56, 59, 25, 89, 53]
counter = len(lista)
print(counter)
p = int(counter / 2)
listb = lista[:p] # копіюємо в новостворений спаисок першу половину старого списку
print(listb)
listc = lista[p:] # копіюємо в новостворений спаисок другу половину старого списку
print(listc)
res = input("Бажаєте зберегти дані у файл - натисніть y, або n щоб вийти з програми\n")
if res == "y":
    with open("task4.txt", "w") as file:
        print(listb, file=file)
        print(listc, file=file)
