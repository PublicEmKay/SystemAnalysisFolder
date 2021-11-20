class Input(object):
    def __init__(self, adress):
        """Constructors"""
        self.adress = adress
    
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