from Laba01.Input import Input


class List(Input):
    def __init__(self):
        """Constructors"""
        self.list

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

        