

#Відкриття файлу input.txt для читання
adress = "/home/emkay/Документи/SystemAnalysisFolder/Laba01/input.txt"

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



