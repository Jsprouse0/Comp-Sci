# Author: Jacob Sprouse
# Assignment Title: Program 9
# Assignment Description: Output Values in a List
# Due Date: 05/04/2023
# Date Created: 05/03/2023
# Date Last Modified: 05/04/2023

# def get_user_values()
# **************************************************************************************
# Description: will take int input into a list and append any new int input            *
# return: integer                                                                      *
# precondition: user must input integers                                               *
# postcondition: returns list of integers and threshold                                *
#                                                                                      *
# **************************************************************************************

# def ints_less_than_or_equal_to_threshold()
# **************************************************************************************
# Description: will take int from process and append at v in loop if <= upperlimit     *
# return: integer                                                                      *
# precondition: user must input integers in previous function                          *
# postcondition: returns list of integers below threshold in list                      *
#                                                                                      *
# **************************************************************************************


def get_user_values():
    data = []
    count = int(input())

    for n in range(0, count):
        num = int(input())
        data.append(num)

    threshold = int(input())
    return data, threshold


def ints_less_than_or_equal_to_threshold(val, upper_limit):
    list_of_num = []
    for v in val:
        if v <= upper_limit:
            list_of_num.append(v)
    return list_of_num


if __name__ == '__main__':
    user_values, upper_threshold = get_user_values()
    res_values = ints_less_than_or_equal_to_threshold(user_values, upper_threshold)

    for value in res_values:
        print(value)
