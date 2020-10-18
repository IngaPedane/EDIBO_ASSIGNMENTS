# Fibonači skaitļu daudzums pēc pieprasījuma
x=int(input("Cik Fibonači skaitļus attēlot? "))
#check = False
#while not check:
while True:
#    try:
#        x=int(input("Cik Fibonači skaitļus attēlot? "))
#        check = True
#        while x < 0:
    val = int(x)
    x=int(input("Ievadīt pozitīvu, reālu skaitli: "))
#        check = False
     except ValueError:
#         try:
#if type(x) != int:
            x=int(input("Ievadītā vērtība nav skaitlis! Mēģiniet vēlreiz: "))
#            check = False
# Pirmie divi skaitļi
#n1, n2 = 0, 1
#count = 0

# Vai ievadītais skaitlis ir pozitīvs reāls skaitlis?
#x=int(input("Cik Fibonači skaitļus attēlot? "))
#if x <= 0:
#    check = False
#    while not check:
#        try:
######### Pārveidot par nebeidzamu loop, kamēr netiks ievadīts poz., reāls skaitlis!!!
#    print("Ievadīt pozitīvu, reālu skaitli: ")
#            x=int(input("Ievadīt pozitīvu, reālu skaitli: "))

#elif x == 1:
#   print(0)
#else:

######### Kā izprintēt loop mainīgos vienā rindā? #########
#    print("Pieprasīti",x,"fibonači skaitļi: ")
#    while count < x:
#print(n1)
#nth = n1 + n2
#n1 = n2
#n2 = nth
#count += 1
