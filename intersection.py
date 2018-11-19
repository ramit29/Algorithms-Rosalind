#!/usr/bin/env python3

a=[7,8,25,72,3,4,5,0,100]

b=[72,1,9,6,3,4,0,6,2,100,0,9,3]

a.sort()
b.sort()
i=0
j=0
intersection=[]
while i < len(a) and j < len(b):
    if a[i] == b[j]:
        intersection.append(a[i])
        i=i+1
    else:
        if a[i] > b[j]:
            j=j+1
        else:
            i=i+1
print(intersection)
