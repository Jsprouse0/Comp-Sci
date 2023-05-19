# Author: Jacob Sprouse
# Assignment Title: Program 4
# Assignment Description: Painting a wall
# Due Date: 05/12/2023
# Date Created: 04/21/2023
# Date Last Modified: 05/09/2023
from math import ceil

# constants
PAINT_PER_GALLON = 350
TAX = 0.07

# Input
wall_height = float(input())
wall_width = float(input())
cost_of_paint_can = float(input())

# Process
wall_area = wall_height * wall_width
paint_needed = wall_area / PAINT_PER_GALLON
cans_needed = ceil(paint_needed)
total_paint_cost = cost_of_paint_can * cans_needed
sales_tax = total_paint_cost * TAX
total_cost = sales_tax + total_paint_cost

# Output
print(f"Wall area: {wall_area:.1f} sq ft")
print(f"Paint needed: {paint_needed:.3f} gallons")
print(f"Cans needed: {cans_needed} can(s)")
print(f"Paint cost: ${total_paint_cost:.2f}")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Total cost: ${total_cost:.2f}")
