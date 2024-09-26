#p5
from wsgiref.util import request_uri

from In_Class.InClassWeek4 import aList


def listOfSquares(aList):
    list2=[]
    for i in aList:
        list2.append(i**2)
    return list2

print(listOfSquares([1,-1,2,3]))

#p6
def discount(alist):
    list2=[]
    for i in alist:
        list2.append(round(i-(i*0.5),1))
    return list2

print(discount([10.2 , 22.48 , 11.37 , 50.11]))

#p7
def sumOfOddIndexes(aList):
    suma=0
    for i in range(0,len(aList)):
        if(i%2!=0):
            suma+=aList[i]
    return suma
print(sumOfOddIndexes([1 , 2 , -3 , 4 , 5]))
#p8
def longWord(aList):
    list2 = []
    for i in aList:
        if len(i)>3:
            list2.append(i)
    return list2
print(longWord([" hello ", "hi", " three ", " kitty "]))
#p9
def countOccurrences(aList, element):
    count=0
    for i in aList:
        if(i==element):
            count+=1
    return count
print(countOccurrences([1 , 1 , 0 , -2 , 1] , 1))
#p10
def removeOccurrences(alist,ele):
