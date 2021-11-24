class Sorting(object):
    def __init__(self):
        """Constructors"""
        self.methodsort
        self.sortreverse

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
