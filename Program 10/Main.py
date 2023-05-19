'''
Author: Jacob Sprouse
Assignment title: Program 10
Assignment Description: Toll Calculator
Due Date: 05/12/2023
Date Created: 05/12/2023
Date Last Modified: 05/12/2023
'''

# def calc_toll()
# *******************************************************************************************
# Description: Function that takes hour, time of day, and weekend to find toll for that day *
# return: float variable toll                                                               *
# pre-condition: parameter hour is a float and is_morning/is_weekend are boolean            *
# post-condition: returns the toll (as a float) for the day                                 *
#                                                                                           *
# *******************************************************************************************


def calc_toll(hour, is_morning, is_weekend):
    # Weekend Toll
    if is_weekend:
        if is_morning:
            if hour < 7:
                toll = 1.05
            else:
                toll = 2.15
        else:
            if hour < 8:
                toll = 2.15
            else:
                toll = 1.10
    # Weekday Toll
    else:
        if is_morning:
            if hour < 7:
                toll = 1.15
            elif hour < 10:
                toll = 2.95
            else:
                toll = 1.90
        else:
            if hour < 3:
                toll = 1.90
            elif hour < 8:
                toll = 3.95
            else:
                toll = 1.40

    return toll


# Output
if __name__ == '__main__':
    print(calc_toll(8, True, False))
    print(calc_toll(1, False, False))
    print(calc_toll(3, False, True))
    print(calc_toll(5, True, True))
