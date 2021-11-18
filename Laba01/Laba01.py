

#Відкриття файлу input.txt для читання
#adress = "/home/emkay/Документи/SystemAnalysisFolder/Laba01/input.txt"

#Метод повертає вкладений список з файлу
def listinput(adress):

    #Створення списку
    list = []

    #Читання інформації з файлу
    with open(adress,'r') as f:
        for line in f:
            lines = []
            for word in line.split():
                lines.append(word)
            list.append(lines)
    return list

#Метод повертає числове значення, необхіне для вибору методу сортування
def userinput():
    n = input('Сортувати за прізвищем(1), сортувати за іменем(2), сортувати по батькові(3), сортувати за номером телефону(4):\n')
    n = int(n)-1
    return n

#Метод повертає булеве значення
def userinputsort():
    n = input('Сортувати за зростанням(1), за спаданням(0):\n')
    n = int(n)
    if n == 1:
        return False
    else:
        return True

#Метод повертає адресу файлу
def userinputfile():
    n = input('Вкажіть повну адресу файлу для сортування:\n')
    return n

#Метод виводить текст на консоль
def outputlist(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            print(list[i][j], end = ' ')
        print()

#Метод виводить вкладений список до файлу
def outputlisttofile(list):
    n = input('Вкажіть повну адресу файлу для запису:\n')
    with open(n, "w") as file:
        print(*list, file=file, sep="\n")
        #file.write(",".join(map(str, list))+"\n")

adress = userinputfile()
list = listinput(adress)
outputlist(list)
methodsort = userinput()
sortreverse = userinputsort()

#Сортування списку
list.sort(key=lambda i: i[methodsort], reverse=sortreverse)
outputlist(list)

what = input('Вивести список до файлу?(y/n)\n')
if what == 'y':
    outputlisttofile(list)
    print('Дякую за те, що скористалися даною програмою. Для виходу натисніть Enter')
    print()
else:
    print('Дякую за те, що скористалися даною програмою. Для виходу натисніть Enter')
    print()  



