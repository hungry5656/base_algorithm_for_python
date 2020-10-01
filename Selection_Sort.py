# ! /usr/bin/env python
# -*- coding:utf-8 -*-

def Find_Smallest(Ar):
    Smallest_E = Ar[0]
    Smallest_index = 0
    for i in range(1,len(Arr)):
        if Arr[i] < Smallest_E:
            Smallest_E = Ar[i]
            Smallest_index = i
    return Smallest_index

def Selection_Sort(Ar):
    NewArr = []
    for i in range(len(Ar)):
        smallest_E = Find_Smallest(Ar)
        NewArr.append(Ar.pop(smallest_E))
    return NewArr
