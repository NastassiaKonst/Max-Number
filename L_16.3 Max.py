def myMAX(list1):
    maxi = list1[0]
    for i in list1:
        if maxi<i:
            maxi=i
    return maxi

a = [1,23,325,2,543,2,9]
print(myMAX(a))

def myMAX(list1):
    maxi = list1[0]
    for i in list1:
        if maxi<i:
            maxi=i
    return maxi

a = [1,23,325,2,543,2,9,56,56,7,56]
print(myMAX(a))
print(myMAX([1,2,3,4,5]))