# definēju funkciju, kura kārtos vērtības augošā secība
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
### https://www.youtube.com/watch?v=5KjapFQNxUo

nums = list(map(int, input("Ievadiet veselus skaitļus (arī negatīvus): ").split()))

sort(nums)
print("Ievadītie skaitļi augošā secībā: ",nums)
### https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
