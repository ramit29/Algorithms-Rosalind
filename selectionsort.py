#!/usr/bin/env python3

def selectionsort(list):

    for i in range(len(list)):
        index=i
        for j in range(i+1,len(list)):
            if list[index] > list[j]:
                index=j
        list[i],list[index]=list[index],list[i]

    return list
print(selectionsort([3,2,5,4,7,2,4,6,2,43,2,5]))
