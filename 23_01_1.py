number = [55, 56, 10, 25, 555, 28, 289, 56, 59, 25, 89]
minelem = (min(number)) # визначаємо найменший елемент списку
i = number.index(minelem) # визначаємо індекс найменшого елементу списку
maxelem = (max(number)) # визначаємо найбільший елемент списку
b = number.index(maxelem) # визначаємо індекс найбільшого елемент списку

temp = number[i] # тимчасовій змінній присвоюємо значення найбільшого елемента
number[i] = number[b] # переносимо на місце більшого менший елемент
number[b] = temp # переносимо на місце мешого більший елемент
print(number)
res = input("Бажаєте зберегти дані у файл - натисніть y, або n щоб вийти з програми\n")
if res == "y":
    with open("task1.txt", "w") as file:
        print(number, file=file)
