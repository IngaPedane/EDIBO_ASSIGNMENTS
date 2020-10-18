class NavPozitivsSkaitlis(UserWarning): 
	pass 
 
while True: 
	x = input("Ievadiet pozitīvu skaitli: ") 
	try: 
		x = int(x) 
		if x <= 0: 
			raise NavPozitivsSkaitlis 
		break 
	except ValueError: 
		print("Ievadītā vērtība nav skaitlis! Mēģiniet vēlreiz: ") 
	except NavPozitivsSkaitlis: 
		print("Ievadītā vērtība nav pozitīvs skaitlis! Mēģiniet vēlreiz: ")
		
### https://www.quora.com/How-can-I-make-sure-the-user-inputs-a-positive-integer-in-Python

#Pirmie divi skaitļi
n1, n2 = 0, 1
count = 0

print("Pieprasīti",x,"fibonači skaitļi: ")
while count < x:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
### https://www.programiz.com/python-programming/examples/fibonacci-sequence
