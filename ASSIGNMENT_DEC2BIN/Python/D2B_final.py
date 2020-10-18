class NavPozitivsSkaitlis(UserWarning): 
	pass
      
def binary(n):
   if n > 1:
       binary(n//2)
       print(n % 2,end = '')
       
while True: 
	dec = input("Ievadiet pozitīvu skaitli: ") 
	try: 
		dec = int(dec) 
		if dec <= 0: 
			raise NavPozitivsSkaitlis 
		break 
	except ValueError: 
		print("Ievadītā vērtība nav skaitlis! Mēģiniet vēlreiz: ") 
	except NavPozitivsSkaitlis: 
		print("Ievadītā vērtība nav pozitīvs skaitlis! Mēģiniet vēlreiz: ")
        
### https://www.quora.com/How-can-I-make-sure-the-user-inputs-a-positive-integer-in-Python

print("Skaitļa",dec,"ievadītā vērtība ir: ")
binary(dec)

