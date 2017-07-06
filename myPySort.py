list1 = [1,2,4,3,7,3,2,1,6,5,4,3,5,6,7,6,5,8,9,10,9,9,9,10]

def mySort(list1):
    for i in range(len(list1)):
        for i in range(len(list1)-1):
            if list1[i] > list1[i+1]:
                list1[i], list1[i+1] = list1[i+1], list1[i]
    print list1

mySort(list1)                    
                
