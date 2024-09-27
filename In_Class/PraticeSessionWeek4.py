#p5

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
    list2=[]
    for i in range(0,len(alist)):
        if(alist[i]!=ele):
            list2.append(alist[i])
    return list2
print(removeOccurrences([0 , " test ", 1 , " apple ", 0 , 1.1] , 0))
#P12
def average(alist):
    suma=0
    count=0
    for i in range(0,len(alist)):

        if(alist[i]%2!=0):
          suma+=alist[i]
          count+=1
    return suma/count


print(average([99 , 89 , 74 , 63 , 100 , 100]))
#p13
def mix(alist):
        temp=alist[0]
        alist[0]=alist[-1]
        alist[-1]=temp
        return alist

print(mix([3 , 2 , 1 , 4]))


def addlists(alist,blist):
    nlist=alist+blist
    print(nlist)
    j=0
    while j<len(nlist)-1:
        if nlist[j]>nlist[j+1]: #checks if bounds at index i is greater than bounds at index i + 1
            temp=nlist[j+1] #if true it sets a temporary variable = to bounds at index i+1
            nlist[j+1]=nlist[j] # then sets bounds i to bounds i + 1  and bounds i to temp
            nlist[j]=temp
            j=0 #resets the sequence to check if the previous number is bigger as well, i know it's not most efficient way to do that
        else :
            j+=1# moves to the next index in the loop
        print(j)
    return nlist


print(addlists([-1,2,3],[2,-3,4]))