

#Відкриття файлу input.txt для читання
adress = "/home/emkay/Документи/SystemAnalysisFolder/Laba01/input.txt"

#Дізнаємося кількість рядків в файлі
lines = 0
with open(adress) as f:
    for line in f:
        lines = lines + 1
print(lines)

#Кількість стовбчиків статична та стандартна
column = 4
#Читання інформації з файлу

