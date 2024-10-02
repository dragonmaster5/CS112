#p1
"""
 Write a function filter positive even(numbers) that takes a list of integers
and returns a new list containing only the positive even numbers.
"""
import math

from In_Class.InClassWeek5 import alist


def filterEven(alist):
    blist=[]
    for i in alist:
        if i%2==0 and i>0:
            blist.append(i)
    return blist

print(filterEven([1 , -2 , -3 , 4 , 5 , 6]))
#p2
'''
Write a function named is empty(a list) that returns True if the list is empty
and False otherwise.'''
def isEmpty(alist):
    return len(alist)==0

print(isEmpty([1,2]))
print(isEmpty([]))

#p3
'''
Write a function named multiply factor(a list, factor) that returns a list where
each element in the original list is multiplied by the given factor. For example
multiply_factor ([1 , 2 , -3] , 2)'''
def multiplyFactor(alist,factor):
    blist=[]
    for i in alist:
        blist.append(i*factor)
    return blist

print(multiplyFactor([1 , 2 , -3] , 2))
#p4
'''Write a function named numeric values(a list) that takes a list as input and
returns a new list with only the numeric elements. Numeric values include both integers
and floating-point numbers. For example:numeric_values (["1", " apple ", 1 , 1.2 , -4])
should return [1, 1.2, −4].
'''
def numericValues(alist):
    blist=[]
    for i in alist:
        if type(i) is type(0) or type(i) is type(0.0):
            blist.append(i)
    return blist
print(numericValues(["1", " apple ", 1 , 1.2 , -4]))

#p5
''' Write a function named remove element(a list, element) that takes a list and
an element as input and returns a new list with all occurrences of that element removed.
For example
removed_element ([0 , " test ", 1 , " apple ", 0 , 1.1] , 0)'''
def removedElement(alist,ele):
    blist=[]
    for i in alist:
        if i != ele:
            blist.append(i)
    return blist


print(removedElement([0 , " test ", 1 , " apple ", 0 , 1.1],0))
#p6
'''. Write a function uppercase strings(a list) that takes a list of strings and
returns a new list with all the strings in uppercase. For example'''
def uppercaseStrings(alist):
    blist=[]
    for i in alist:
        blist.append(i.upper())
#P7
'''
Write a function last names(full names) that takes a list of full names and
returns a new list containing all last names. Here, we assume that each full name consists
of a first name followed by a last name, separated by a space. For example,
1
last_names ([" Anne Nguyen ", " David Hilbert ", " Michael Jordan ", "
Alan Turing "])
should return [“Nguyen”, “Hilbert”, “Jordan”, ”Turing”]. All of these individuals are
famous, except for the first one (at least for now!).'''
def lastName(fullNames):
    blist=[]
    for i in fullNames:
        blist.append(i.split()[-1])
    return blist
print(lastName(["Anne Nguyen", "David Hilbert", "Michael Jordan", "Alan Turing"]))
#p8
'''Write a function join strings(a list) that takes a list of strings and joins them
into a single string, separated by spaces.
join_strings (["I", " Love ", " Lake ", " Forest ", " College "])
should return “I Love Lake Forest College”.'''
def joinStrings(alist):
    concatString=""
    for i in alist:
        concatString+=i
    return concatString
#p9
'''Write a function longest string(a list) that takes a list of strings and returns
the longest string. For example
longest_string ([" apple ", " banana ", " mango "])
should return “banana”.'''
def longestString(alist):
     maxa=0
     for i in range(0,len(alist)):
         if (len(alist[i]))>len(alist[maxa]):
             maxa=i
     return alist[maxa]
print(longestString([" apple ", " banana ", " mango "]))
#p10
'''
Given a list of circle radii, create a new list containing the corresponding
areas of the circles, rounded to one decimal place. For example, if the list is
radii = [1 ,2 ,3]
''' import math
list1=[1,2,3]
list2=[round(math.pi*(i**2),1) for i in list1]
print(list2)
#p11
'''From a list of integers, create a new list that includes only the odd numbers
using list comprehension. For example, if the given list is [1, 2, 3, 4, 5, 6], then the new
list should be [1, 3, 5]'''
intlist=[1,2,3,4,5,6]
intlist2=[i for i in intlist if i%2!=0]
print(intlist2)
#p12
'''2. From a list of strings, create a new list that contains the first letter of each
string. For example, if the given list is [“Apple”, “Banana”, “Mango”], the new list should
be [“A”, “B”, “M”].
'''
stringList=["Apple", "Banana", "Mango"]
stringList2=[i[0] for i in stringList]
print(stringList2)
#p13
'''Given a list of words, create a new list containing only those words that are
shorter than 4 characters. For example, if the list is [“Ant”, “Dog”, “Lion”, ”Fish”]), the
new list should be [“Ant”, “Dog”]'''
WordList= ["Ant","Lion","Dog","Fish"]
WordList2=[i for i in WordList if len(i)<4]
print(WordList2)