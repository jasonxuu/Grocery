#!/usr/bin/env python
# coding=utf-8 

global alist

def find_partition_point(alist, first, last):
    basic_value = alist[first]
    
    left_mark = first + 1
    right_mark = last

    while True:
        while alist[left_mark] <= basic_value and left_mark <= right_mark:
            left_mark += 1
        while alist[right_mark] >= basic_value and right_mark >= right_mark:
            right_mark -= 1

        if left_mark > right_mark:
            break

        else:
            temp = alist[left_mark]
            alist[left_mark] = alist[right_mark]
            alist[right_mark] =  temp

    temp = alist[first]
    alist[first] = alist[right_mark]
    alist[right_mark] = temp
    return right_mark

def sort_recursion(alist, first, last):
    if first < last:
        pos = find_partition_point(alist, first, last)

        sort_recursion(alist, first, pos-1)
        sort_recursion(alist, pos+1, last)


if __name__ == '__main__':
    alist = []
    sort_recursion(alist, 0, len(alist)-1)
