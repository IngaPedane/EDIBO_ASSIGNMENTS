# definēju funkciju, kura kārtos vērtības augošā secība
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
### https://www.youtube.com/watch?v=5KjapFQNxUo

"""inputs = []
while True:
    inp = raw_input()
    if inp == "":
        break
    inputs.append(int(inp))
    
nums = [5, 3, 8, 6, 7, 2]
sort(nums)

print(nums)"""

numbers = input("Ievadiet skaitļus (pozitīvus un negatīvus): ")
items = [int(num) for num in numbers.split()]
### https://stackoverflow.com/questions/27492499/sort-a-user-input-list-of-numbers-using-python-bubble-sort

sort(nums)
print(nums)
