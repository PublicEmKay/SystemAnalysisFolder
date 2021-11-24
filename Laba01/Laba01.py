#Версія програми ждя сортування 2.0
#Потрібно виправити проблеми з імпортом модулів
#Тимчасово класи перенесено до одного файлу

class Input(object):
    def __init__(self):
        """Constructors"""
        self.adress
    
    #Метод повертає адресу файлу
    def userinputfile(self):
        n = input('Вкажіть повну адресу файлу для сортування:\n')
        self.adress = n

    #Метод повертає вкладений список з файлу
    def listinput(self):

        #Створення списку
        list = []

        #Читання інформації з файлу
        with open(self.adress,'r') as f:
            for line in f:
                lines = []
                for word in line.split():
                    lines.append(word)
                list.append(lines)
        return list

class Output(object):
    def __init__(self, list):
        """Constructors"""
        self.list = list
    
    #Метод виводить текст на консоль
    def outputlist(self):
        for i in range(len(self.list)):
            for j in range(len(self.list[i])):
                print(self.list[i][j], end = ' ')
            print()

    #Метод виводить вкладений список до файлу
    def outputlisttofile(self):
        n = input('Вкажіть повну адресу файлу для запису:\n')
        with open(n, "w") as file:
            print(*self.list, file=file, sep="\n")
            #file.write(",".join(map(str, self.list))+"\n")
            

class Sorting(object):
    def __init__(self):
        """Constructors"""
        self.methodsort = 0
        self.sortreverse = False

    #Метод повертає числове значення, необхіне для вибору методу сортування
    def userinput(self):
        n = input('Сортувати за прізвищем(1), сортувати за іменем(2), сортувати по батькові(3), сортувати за номером телефону(4):\n')
        n = int(n)-1
        self.methodsort = n

    #Метод повертає булеве значення
    def userinputsort(self):
        n = input('Сортувати за зростанням(1), за спаданням(0):\n')
        n = int(n)
        if n == 1:
            self.sortreverse = False
        else:
            self.sortreverse = True

    #Повертає атрибут methodsort
    def get_methodsort(self):
        return self.methodsort

    #Повертає атрибут sortreverse
    def get_sortreverse(self):
        return self.sortreverse


class List(Input):
    def __init__(self):
        """Constructors"""
    list

    #Метод повертає вкладений список з файлу
    def listinput(self):

        #Створення списку
        list = []

        #Читання інформації з файлу
        with open(self.adress,'r') as f:
            for line in f:
                lines = []
                for word in line.split():
                    lines.append(word)
                list.append(lines)
        self.list = list
    
    #Повернути список
    def getList(self):
        return self.list

        
#Відкриття файлу input.txt для читання
#adress = "/home/emkay/Документи/SystemAnalysisFolder/Laba01/input.txt"

list = List()
list.userinputfile()
list.listinput()
listoutput = Output(list.getList())
listoutput.outputlist()
listsort = Sorting()
listsort.userinput()
listsort.userinputsort()

#Сортування списку
list.getList().sort(key=lambda i: i[listsort.get_methodsort()], reverse=listsort.get_sortreverse())
listoutput = Output(list.getList())
listoutput.outputlist()

what = input('Вивести список до файлу?(y/n)\n')
if what == 'y':
    listoutput.outputlisttofile()
    print('Дякую за те, що скористалися даною програмою. Для виходу натисніть Enter')
    input()
else:
    print('Дякую за те, що скористалися даною програмою. Для виходу натисніть Enter')
    input()  



