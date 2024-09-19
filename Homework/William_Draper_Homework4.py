#p1
"""Determine the output of the following code:
(1) my_str = ’The cat in the hat ’
print ( my_str [0:3])
(2) my_str = ’The cat in the hat ’
print ( my_str [3:7])
(3) my_str = ’http :// reddit .com /r/ python ’
print ( my_str [17: -2])
(4) my_str = ’http :// reddit .com /r/ python ’
protocol = ’http :// ’
print ( my_str [len( protocol ) :])"""
#1) "the"
#2)"the cat"
#3) "/r/pyth"
#4) reddit.com/r/python
#p2
'''Write a function called odd sum(a list) that takes a list of integers as an
input. The function will return the sum of all odd numbers in the list. For example
odd_sum ([ -1 , 2 , -4 , 3 , 5])
should return 7.'''
def oddSum(n):
    suma=0
    for i in n:
        if(i%2!=0):
            suma+=i
    return suma
#print(oddSum([ -1 , 2 , -4 , 3 , 5]))
#p3
'''
Write a function called count string(a list) that takes a list and returns the
number of strings in the list. For example
countString ([" Hello ", 4 , "5", 5.5])
'''
def countString(n):
    count=0
    for i in n:
        if type(i)== type(""):
            count+=1
    return count
#print(countString([" Hello ", 4 , "5", 5.5]))
#p4
'''
Write a function print characters(s) that takes a string and prints each vowel
character on a new line.
'''
def printVowelGroups(n):
    vowels=["a","e","i","o","u","y"]
    index =0
    for i in n:
        index+=1
        for j in vowels:
            if(i==j):
                print(j)
                break
printVowelGroups("banana")
#p5
'''
Write a function called first equal last(string) that takes a string as a string as
input and returns True if the first and last characters of this string are the same. Otherwise,
return False. For example,
first_equal_last (" hello ")
should return False while
'''
def firstEqualsLast(n):
    return n[0]==n[len(n)-1]
print(firstEqualsLast("racecar"))
#p6
'''
'''