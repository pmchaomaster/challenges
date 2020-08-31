def mergeList(list1,list2):

    i1=0
    i2=0
    newList=[]

    while len(list1)>i1 or len(list2)>i2:
        if i2==len(list2) or (i1<len(list1) and list1[i1] <= list2[i2]):
            newList.append(list1[i1])
            i1 +=1
        else:
            newList.append(list2[i2])
            i2+=1

    return newList


list1 = [-1,3,5,7,9]
list2 = [2,4]

result = mergeList(list1,list2)

print (result)
