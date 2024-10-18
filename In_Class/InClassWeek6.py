


def search(alist,ele):
    for i in alist:
        if(i==ele):
            return True
    return False

def binarySearch(aList,high,low,ele):
        if high>=low:
            mid=(high+low)//2
            if aList[mid]==ele:
                return mid
            elif ele>mid:
                return binarySearch(aList,mid-1,low,ele)
            else:
                return binarySearch(aList,high-1,mid,ele)
        else:
            return -1
print(binarySearch([i for i in range(0,101)],101,0,33))

def sumUpToN(n):
    if n==0:
        return n
    return n+sumUpToN(n-1)

print(sumUpToN(3))

def sum_list(aList):

    if len(aList)==1:
        return aList[0]
    return aList.pop()+sum_list(aList)

print(sum_list([1,2,3,-4,5]))

def power(base,exp):
    if exp==1:
        return base
    return base*power(base,exp-1)
print(power(4,3))
def reverseString(s):
    if len(s)==0:
        return
    return s[0]+reverseString(s[-1:])
#print(reverseString("Hello"))

def getFirstName(FullName):
    name =FullName.split()[0]
    return name
def sortByFirstName(Alist):
    return sorted(Alist,key=getFirstName)
print(sortByFirstName( ["David Hilbert ",  "Alan Turing ", "Forest Gump "]))


def recursiveSumOfSquares(n):
    if n==0:
        return n
    return n**2+recursiveSumOfSquares(n-1)
print(recursiveSumOfSquares(3))

def recursiveSumOfEven(n):
    if n>0:
        x=(n*2)-1
        return x+recursiveSumOfEven(n-1)
    return 0

print(recursiveSumOfEven(3))

def recursiveSumOfEvenList(Alist):
    if len(Alist)==1:
        return Alist[0]
    temp=Alist.pop()
    if temp%2==0:
        return temp+recursiveSumOfEvenList(Alist)
    return recursiveSumOfEvenList(Alist)
print(recursiveSumOfEvenList([10,2,3,4,5,6]))
