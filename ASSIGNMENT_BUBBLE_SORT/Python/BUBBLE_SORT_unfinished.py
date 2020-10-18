# definēju funkciju, kura kārtos vērtības augošā secība
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
### https://www.youtube.com/watch?v=5KjapFQNxUo
"""
inputs = []
while True:
    inp = raw_input()
    if inp == "":
        break
    inputs.append(int(inp))
    
nums = [5, 3, 8, 6, 7, 2]
sort(nums)

print(nums)
"""

"""
nums = int(input("Ievadiet skaitļus (pozitīvus un negatīvus): "))
items = [int(nums) for nums in nums.split()]
### https://stackoverflow.com/questions/27492499/sort-a-user-input-list-of-numbers-using-python-bubble-sort

sort(int(nums))
print(nums)
"""

nums = list(map(int, input("Enter a multiple value: ").split()))
sort(nums)
print(nums)
### https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
