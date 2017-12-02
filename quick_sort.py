# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 13:21:03 2017

@author: libing

Quick sort is a kind of sorting algorithm using a divide and conquer strategy
to put a sequence(list) divided into two sub-sequences(sub-list).
    average condition: O(nlogn)
    the worst condition: O(n*n)
    the best condition: O(nlogn)
"""


def quick_sort(array):  # array: list
    less = []
    greater = []
    if len(array) < 1:
        return array
    pivot = array.pop()  # select a pivot to divide sequence
    for x in array:
        if x < pivot:
            less.append(x)
        else:
            greater.append(x)
    return quick_sort(less) + [pivot] + quick_sort(greater)  # recursion
