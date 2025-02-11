#!/usr/bin/env python3

def print_fibonacci(length):
    my_list = []

    if length > 0:
        my_list.append(0)
    if length >= 2:
        my_list.append(1)
    
        for i in range(2, length):
            sequence = my_list[-1] + my_list[-2]
            my_list.append(sequence)
    
    return print(my_list)
