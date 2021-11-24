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
            