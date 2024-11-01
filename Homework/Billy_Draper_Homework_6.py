#P1
'''Write a function named three largest(alist) that takes a list of numbers as
input. The function should return a list containing the three largest values from alist,
sorted from lowest to highest. If the list contains fewer than three numbers, return the
original list sorted from lowest to highest. For example
three_largest ([8 , 3 , 1 , 9 , 12])'''
def three_largest(aList):
    Slist=sorted(aList)
    return [Slist[len(Slist)-3],Slist[len(Slist)-2],Slist[-1]]
print(three_largest([8 , 3 , 1 , 9 , 12]))
#P2
''' Write a function named find median(alist) that takes a list of numbers alist
as input. The function should return the median value of this list. Recall that the median
is defined as follows
• If the list has an odd number of elements: The median is the middle value in the
sorted list.
• If the list has an even number of elements: The median is the average of the two
middle values'''

def findMedian(alist):
    slist=sorted(alist)
    if len(slist)%2!=0:
        return slist[len(slist)//2]
    else:
        mAvg=(slist[len(slist)//2]+slist[(len(slist)//2)-1])//2
        return mAvg

print(findMedian([7 , 1 , 4]))
print(findMedian([7 , 1 , 4 , 6]))
#P3
'''Write a function named sort by price(products) that takes a list of tuples,
where each tuple contains a product name and its price (e.g., (”apple”, 1.50)). The function
should return a new list of these products sorted by their price. For example
sort_by_price ([(" banana ", 1.5) , (" apple ", 2.91) , (" orange ", 2.25)
])
should return
[(" banana ", 1.5) , (" orange ", 2.25) , (" apple ", 2.91) ].
1
To solve this problem, you need to create another function say, get price(a product) that
takes a product as an input and returns its price. See the practice problem file for some
more similar examples'''
def getPrice(Product):
        return Product[-1]
def sortByPrice(Products):
    sProducts=sorted(Products,key=getPrice)
    return sProducts
print(sortByPrice(([(" banana ", 1.5) , (" apple ", 2.91) , (" orange ", 2.25)
])))
#P4
''' Write a function named sort names(name list) that takes a list of names
name list as input. The function should return a new list with these names sorted in
alphabetical order, ignoring case sensitivity (recall that, in Python lowercase letters are
greater than all uppercase letters.) For example
sort_names ([" anne ", " charlie ", " David ", " Armin "])
should return [”anne”, ”Armin”, ”charlie”, ”David”].
'''
def sort_names(alist):
    for i in range(0,len(alist)-1):
        if(alist[i].lower()>alist[i+1].lower()):
            temp= alist[i]
            alist[i]=alist[i+1]
            alist[i+1]=temp
            sort_names(alist)
    return alist
print(sort_names([" anne ", " charlie ", " David ", " Armin "]))

#p5
'''Write a function named sort title(alist) that takes a list of book titles as
input. The function should return a new list with these titles sorted by the number of
words in each title. For example
alist = ["For whom the bell tolls ",
"The old man and the sea",
" Please look after mom",
" Siddhartha "]
print ( sort_title ( alist ) )
should return
[" Siddhartha ", " Please look after mom", "For whom the bell tolls ",
"The old man and the sea"].
Coincidentally, Siddhartha is also one of my favorite books. Check it out in your free time!'''
def wordAmount(Sentence):
    return len(Sentence.split())

def sortTitle(alist):
    return sorted(alist, key=wordAmount)

print(sortTitle(["For whom the bell tolls ",
"The old man and the sea",
" Please look after mom",
" Siddhartha "]))
#p6
'''. Write a function named choose best book(books and ratings) that takes a
list of tuples, where each tuple contains a book title and its rating. The function should
return the name of the book with the highest rating. For simplicity, assume that all the
ratings are different. For example
books_and_ratings = [(" Siddhartha ", 4.9) ,("The Old Man and the Sea", 4.7) ,("For Whom the Bell Tolls ", 4.8) ,(" Please Look After Mom", 4.6)
]
print ( choose_best_book ( books_and_ratings ) )
should return ”Siddhartha”.
'''
def ratings(bookT):
    return bookT[-1]
def chooseBestBook(BooksAndRatings):
    return sorted(BooksAndRatings,key=ratings)[-1][0]
print(chooseBestBook([(" Siddhartha ", 4.9) ,("The Old Man and the Sea", 4.7) ,("For Whom the Bell Tolls ", 4.8) ,(" Please Look After Mom", 4.6)
]))
#p7
''') Write a function named recursive sum(alist) that takes a list of numbers as input
and returns the sum of the squares of all elements in the list. For example
alist = [1 ,2 , -3]
recursive_sum ( alist )
should return 1^2 + 2^2 + (−3)^2 = 14.

(2) Write another function non recursive sum(alist) to achieve the same goal.'''
#1)
def recursiveSum(alist):
    if len(alist)==1:
        return alist[0]
    temp=alist.pop()**2
    return temp+recursiveSum(alist)
print(recursiveSum([1,2,-3]))
#2)
def sumOfSquares(alist):
    suma=0
    for i in alist:
        suma+=i**2
    return suma
print(sumOfSquares([1,2,-3]))
#p8

'''Write a function name recursive sum power of two(n) that takes a positive integer
n as an input and returns the sum of the first n-powers of 2
1 + 2 + 22 + . . . + 2n−1
.
For example
print ( recursive_sum_power_of_two (4) )
should return 15 because 2^0 + 2^1+2^2 + 2^3 = 15.
(2) Write another non-recursive function to achieve the same goal.
Remark 2.1. Can you predict the general formula for the sum
'''
suma=0
def powersOfTwo(n):
    if n==0:
        return 0
    return 2**(n-1)+powersOfTwo(n-1)
print(powersOfTwo(5))
def nonRecursivePowersOfTwo(n):
    return (2**n)-1
#p9
'''Write a recursive function recursive count vowels(s) that takes a string s as input
and returns the number of vowels (a, e, i, o, u) in s, ignoring case.
(2) Write a non-recursive function to achieve the same goal'''
#1)
def recursiveCountVowels(s):
    if not s:
        return 0
    if s[0].lower()=='a' or s[0].lower()=='e' or s[0].lower()=='i' or s[0].lower()=='o' or s[0].lower()=='u':
        return 1+recursiveCountVowels(s[1:])
    else:
        return recursiveCountVowels(s[1:])

print(recursiveCountVowels("Hello"))
#2)
def countVowels(aList):
    count=0
    for i in aList:
        for j in 'aeiou':
            if i==j:
                count+=1
    return count
print(countVowels("hello"))
#p10
''' Write a recursive function recurive sum of powers(n, k) that computes the sum of
the first n integers raised to the power of k.
1
k + 2k + . . . + n
k
.
For example
sum_of_powers (3 , 2)
should return 14 because 12 + 22 + 32 = 14.
(2) Write a non-recursive version to achieve the same goal.
3
(3) Use list comprehension and one of your functions to calculate the ratio
1
k + 2k + . . . + n
k
nk+1 ,
for k = 3 and n ∈ [10, 102
, 103
, 104
, 105
, 106
].
'''
def recursiveSumOfPowers(n,k):
    if n==1:
        return 1
    return n**k+recursiveSumOfPowers(n-1,k)
print(recursiveSumOfPowers(3,2))

def sumOfPowers(n,k):
    suma=0
    for i in range(0,n+1):
        suma+=i**k
    return suma
print(sumOfPowers(3,2))
#3) Limit approaching zero from the left?
k=3
j=[10,10**2,10**3,10**4,10**5,10**6]

print([(i**k)/i**(k+1) for i in j])
#p11
'''An arithmetic progression is a sequence of numbers such that the difference
from any succeeding term to its preceding term remains constant throughout the sequence.
The constant difference is called the common difference of that arithmetic progression
(often denoted by d). For example
1, 4, 7, 10, 13, . . .
is an arithmetic progression with d = 3. An arithmetic sequence can be defined recursively
as follows
a0 = a, an = an−1 + d.
In the above example, a = 1, d = 3.
(1) Write a recursive function arithmetic sequence(a, d, n) that takes the first team
(a), the difference (d), and the index (n) as input and returns the n-th term of the
corresponding arithmetic sequence. For example
arithmetic_sequence (1 , 3 , 4)
should return 13.
(2) Write a non-recursive function to achieve the same goal. Hint: You can create a
sequence [a0, a1, . . . , an−1] using the append method (creating this list is not absolutely necessary but you might find it more intuitive.)
'''
#1)
def arithmeticSequence(a,d, n):
    if n==0:
        return a
    return d+arithmeticSequence(a,d,n-1)
print(arithmeticSequence(1,3,4))
#2)
def nArithemeticSequence(a,d,n):
    for i in range(0,n):
        a+=d
    return a

print(nArithemeticSequence(1,3,4))
#p12
'''The Lucas sequence is defined as follows, L0 = 2, L1 = 1 and for n ≥ 2
L(n) = L(n − 1) + L(n − 2).
The first few terms of this sequence are
2, 1, 3, 4, 7, 11, . . .
(1) Write a recursive function named lucas(n) that returns that n-th Lucas number.
(2) Write a non-recursive version to achieve the same goal.
So far, we have learned how recursion works for linear recursion. The same principle
works for non-linear recursive relations as well.'''
def recursiveL(n):
    if n==0:
        return 2
    if n==1:
        return 1
    return recursiveL(n-1)+recursiveL(n-2)
print(recursiveL(10))

def l(n):
    """Generates the first n numbers of the Lucas series."""
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    a, b = 2, 1
    result = [a, b]
    for i in range(2, n+1):
        c = a + b
        result.append(c)
        a, b = b, c

    return result[n]
print(l(5))
#p13
'''t an be the sequence defined as follows
a(0) = 1, a(n) = a(n − 1)^2 + 1.
The first few terms of this sequence are
1, 2, 5, 26, 677 . . .
(1) Write a recursive function named sequence a(n) that returns that n-th term of this
sequence.
(2) Write a non-recursive version to achieve the same goal.'''

def recursiveSeries(n):
    if n==0:
        return 1
    return recursiveSeries(n-1)**2+1
print(recursiveSeries(2))
#2)
def a(n):
    if n==0:
        return 1
    result=[1]
    for i in range(0,n+1):
        result.append(result[i]**2+1)
    return result[n]
print(a(3))
#p14
'''. Let an be the sequence defined as follows: b0 = b1 = 1 and
bn =
b
2
n−1 + 2
bn−2
.
The first few terms of this sequence are
1, 1, 3, 11, 41, 153.
(1) Write a recursive function named sequence b(n) that returns that n-th term of this
sequence.
(2) Write a non-recursive version to achieve the same goal.'''
def recursiveB(n):
    if n==0:
        return recursiveB(1)
    if n==1:
        return 1
    return (recursiveB(n-1)**2+2)//recursiveB(n-2)
print(recursiveB(5))

def b(n):
    if n<2:
        return 1
    results=[0,1]
    for i in range(2,n+1):
        results[0]=results[1]
        result=(results[i-1]**2+2)//results[i-2]
        results.append(result)
    return results[n]

print(b(5))
