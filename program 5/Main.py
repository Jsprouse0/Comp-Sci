# Author: Jacob Sprouse
# Assignment Title: Program 5
# Assignment Description: Count Odd numbers
# Due Date: 05/12/2023
# Date Created: 04/24/2023
# Date Last Modified: 05/09/2023

count = 0
odd = 0
calculation = 0

# read 4 integer inputs
numbers = [int(input()), int(input()), int(input()), int(input())]

# Process
for count in range(len(numbers)):
    calculation = numbers[count] % 2
    if calculation == 1:
        odd += 1
    count += 1

# Output
print(odd)



