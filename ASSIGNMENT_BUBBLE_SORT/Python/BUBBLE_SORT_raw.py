# definēju funkciju, kura kārtos vērtības augošā secība
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
### https://www.youtube.com/watch?v=5KjapFQNxUo

#nums = list(map(int, input("Ievadiet veselus skaitļus (arī negatīvus): ").split()))

while True:
    nums = list(map(int, input("Ievadiet veselus skaitļus (arī negatīvus): ").split()))
#    nums = input("Ievadiet pozitīvu skaitli: ") 
    try: 
        nums = int(nums) 
        if nums <= 0: 
            raise NavPozitivsSkaitlis 
        break 
    except ValueError: 
        print("Ievadītā vērtība nav skaitlis! Mēģiniet vēlreiz: ") 
    except NavPozitivsSkaitlis: 
        print("Ievadītā vērtība nav pozitīvs skaitlis! Mēģiniet vēlreiz: ")
        
### https://www.quora.com/How-can-I-make-sure-the-user-inputs-a-positive-integer-in-Python

sort(nums)
print(nums)
### https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
