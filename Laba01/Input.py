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