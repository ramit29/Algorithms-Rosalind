def insertionsort(list):
    for i in range(1,len(list)):
        value=list[i]
        j=i
        while j > 0 and list[j-1] > value:
            list[j]=list[j-1]
            print(list[j])
            j=j-1
        list[j]=value










a=[7,3,2,4]
insertionsort(a)
print(a)
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

list = [54,26,93,17,77,31,44,55,20]
insertionSort(list)
print(list)
