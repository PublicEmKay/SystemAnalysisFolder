import List
import Sorting
import Output

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



