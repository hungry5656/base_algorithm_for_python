# ！/usr/bin/env python
# -*- coding:utf-8 -*-

def Binary_Search(List_Array, Item):
    Low_Index = 0
    High_Index = len(List_Array) - 1
    
    while Low_Index <= High_Index:
        Mid_Index = ( Low_Index + High_Index ) // 2
        Guess_Num = List_Array[Mid_Index]
        if Guess_Num == Item:
            return Mid_Index
        if Guess_Num > Item:
            High_Index = Mid_Index - 1
        else:
            Low_Index = Mid_Index + 1
    return None
