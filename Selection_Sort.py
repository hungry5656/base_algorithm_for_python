# ! /usr/bin/env python
# -*- coding:utf-8 -*-

def Find_Smallest(Arr):
    Smallest_E = Arr[0]
    Smallest_index = 0
    for i in range(1,len(Arr)):
        if Arr[i] < Smallest_E:
            Smallest_E = Arr[i]
            Smallest_index = i
    return Smallest_index

def Selection_Sort(Arr):
    NewArr = []
    for i in range(len(Arr)):
        smallest_E = Find_Smallest(Arr)
        NewArr.append(Arr.pop(smallest_E))
    return NewArr
