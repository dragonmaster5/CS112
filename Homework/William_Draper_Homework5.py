#p1
"""
 Write a function filter positive even(numbers) that takes a list of integers
and returns a new list containing only the positive even numbers.
"""
def filterEven(alist):
    return[i for i in alist if i>0 and i%2==0]

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

    return [i*factor for i in alist]

print(multiplyFactor([1 , 2 , -3] , 2))
#p4
'''Write a function named numeric values(a list) that takes a list as input and
returns a new list with only the numeric elements. Numeric values include both integers
and floating-point numbers. For example:numeric_values (["1", " apple ", 1 , 1.2 , -4])
should return [1, 1.2, −4].
'''
def numericValues(alist):
    return [i for i in alist if type(i) is type(0) or type(i) is type(0.0)]
print(numericValues(["1", " apple ", 1 , 1.2 , -4]))

#p5
''' Write a function named remove element(a list, element) that takes a list and
an element as input and returns a new list with all occurrences of that element removed.
For example
removed_element ([0 , " test ", 1 , " apple ", 0 , 1.1] , 0)'''
def removedElement(alist,ele):
    return[i for i in alist if i!=ele]
print(removedElement([0 , " test ", 1 , " apple ", 0 , 1.1],0))
#p6
'''. Write a function uppercase strings(a list) that takes a list of strings and
returns a new list with all the strings in uppercase. For example'''
def uppercaseStrings(alist):
    return[i.upper() for i in alist]
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
    return [i.split()[-1] for i in fullNames]
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
