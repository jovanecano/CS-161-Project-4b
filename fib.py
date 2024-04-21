# Author: Jovane Cano
# GitHub Username: jovanecano
# Date: 04/20/2024
# Description: This program is contains a function that returns the number within the Fibonacci sequence at the specified position

def fib(position):
    """This function outputs the values within the fibonacci sequences at the point the user specifies"""
    if position <= 2: # for the first 2 values, it returns 1
        return 1
    else:
        # after the second number until the specified value, the function adds the two previous numbers to calculate the current value

        previous = 1
        current = 1
        for fib_num in range(3, position+1):
            previous, current = current, previous+current
    return current

# print(fib(5))