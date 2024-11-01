#Problem 1
#B
#Problem 2
#C
#Problem 3
#A
#Problem 4
#B
#Problem 5
#D
#Problem 6
#B
#Problem 7
#13
#Problem 8
'''Given a list of words, create a new list containing the length of each word
from the original list. For example, for
words = ["hello", "world", "python", "list", "comprehension"]
the result should be
[5 , 5 , 6 , 4 , 13]'''

print([len(i) for i in ["hello", "world", "python", "list", "comprehension"]])
#Problem 9
'''Given a dictionary where the keys are student names and the values are their
years in college, create a new list containing the names of all freshmen. For example for
students = {
" Alice ": 1 ,
"Bob": 2 ,
" Charlie ": 1 ,
" David ": 3 ,
"Eve": 4
}
the output should be
[" Alice ", " Charlie "]'''
print([i for i,v in {" Alice ": 1 ,
"Bob": 2 ,
" Charlie ": 1 ,
" David ": 3 ,
"Eve": 4}.items() if v==1])
#Problem 10
'''Given a tuple of strings, create a new list containing only the strings that
end with the letter ”a”. For example
words = (" banana ", " apple ", " avocado ", " cherry ", " pasta ", " data ")
the result should be
[" banana ", " pasta ", " data "]'''
print([i for i in ["banana", "apple", "avocado", "cherry", "pasta", "data"] if i[-1]=='a' ])
#Problem 11
'''. Write a function named count appearance(a tuple, number) that takes a
tuple of integers and a number as input. The function should return the number of times
that this number appears in the tuple. For example
a_tuple = (1 , 2 , 3 , 2 , 4 , 2 , 5)
number = 2
count_appearance ( a_tuple , number )
should return 3.'''
def countAppearance(aTuple,num):
    count=0
    for i in aTuple:
        if i ==num:
            count+=1
    return count
print(countAppearance((1 , 2 , 3 , 2 , 4 , 2 , 5),2))
#Problem 12
'''Write a function named is increasing(alist) that takes a list of integers as
input. The function should return True if alist is sorted in ascending order (from lowest
to highest); otherwise, it should return False.
print ( is_increasing ([1 , 2 , 3 , 4 , 5]) ) # Output : True
print ( is_increasing ([5 , 3 , 2 , 1]) ) # Output : False
print ( is_increasing ([1 , 2 , 2 , 3 , 4]) ) # Output :'''
def isIncreasing(aList):
    return aList==aList.sort()
#problem 13
'''Write a program that takes a list of words and sorts them by the frequency
of the letter ”e” in each word, from lowest to highest. For example
words = [" apple ", " banana ", " elderberry "]
should return
words = [" banana ", " apple ", " elderberry "]'''

#Problem 14
'''14. Write a program that takes a list of tuples, where each tuple contains two
elements: a string and an integer. Sort the tuples based on the integer value (the second
element of each tuple) from lowest to highest order. Finally, print the sorted list. For
example
tuples_list = [(" apple ", 3) , (" banana ", 1) , (" cherry ", 2) , (" date "
, 5) , (" kiwi ", 4) ]
should return
'''
def sortT(tuples):
    for i in range(0,len(tuples)-1):
        if tuples[i][-1]>tuples[i+1][-1]:
            temp = tuples[i + 1]
            tuples[i + 1] = tuples[i]
            tuples[i] = temp
    return tuples
print(sortT([(" apple ", 3) , (" banana ", 1) , (" cherry ", 2) , (" date "
, 5) , (" kiwi ", 4) ]))

#problem 15
def recursiveSum(alist):
    if len(alist)==1:
        return alist[0]**2
    return alist.pop(0)**2+recursiveSum(alist)
print(recursiveSum([1,2,3,4,5]))
#problem 16
def recursiveSumOfEven(alist):
    if len(alist)==1 and alist[0]%2==0:
        return alist[0]
    elif(len(alist)==1 and alist[0]%2!=0):
        return 0
    temp=alist.pop(0)
    if(temp%2==0):
        return temp+recursiveSumOfEven(alist)
    else:
        return recursiveSumOfEven(alist)
print(recursiveSumOfEven( [1 , 2 , 3 , 4 , 5]))
#problem 17
def a(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return (a(n-1)**2)+(a(n-2)**2)
def A(n):
    for i in range(0,n):
        if n<0:
            return 1
    results=[1,1]
    for j in range(2, n + 1):
        results[0] = results[1]
        result = (results[j - 1] ** 2) +results[j - 2]**2
        results.append(result)
    return results[n]
print(a(4))
print(A(4))
#problem 18
def maxScores(d):
    for i,v in d.items():
        d[i]=max(v)
    return d
print(maxScores( {" Alice ": [85 , 90 , 78] , "Bob ": [92 , 88 , 95]}))
#problem 19
def TopScores(d):
    l=[]
    for i,v in d :
        l.append((i,v))
    j=0
    while j<len(l)-1:
        if l[j][-1]>l[j + 1][-1]:
            temp = l[j + 1]
            l[j + 1] = l[j]
            l[j] = temp
    for i in range(0,len(l)):
        num=l.pop(0)
        if(num[-1])==max(l):
            l.append(num[0])
    return l
print()




