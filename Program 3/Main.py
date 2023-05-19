# Author: Jacob Sprouse
# Assignment Title: Program 3
# Assignment Description: Sum The Digits
# Due Date: 05/12/2023
# Date Created: 04/20/2023
# Date Last Modified: 05/09/2023

addition = 0

# Input
integer = int(input('Enter an integer between 0 and 9999999: '))
print(integer)

# Process
while integer > 0:
    last_num = integer % 10
    addition += last_num
    integer //= 10

# Output
print(f"The sum of the digits is {addition}.")





