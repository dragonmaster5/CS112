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
Write a function called print odd length(a list) that takes a list of strings as
input and prints out all strings with odd lengths in the list. For example
print_odd_length ([ ’apple ’, ’orange ’, ’banana ’])
should print out ’apple’ since it is the only string with odd length'''
def printOddLen(aList):
    for i in aList:
        if(len(i)%2!=0):
           print(i)
#p7
'''
Write a function called numeric sum(a list) that takes a list as input and
returns the sum of all numeric values in the list (a numeric value could be either an integer
or a floating number). For example
numeric_sum ([" Hello ", 5 , 6.1 , " Apple "])
should return 11.1'''
def numericSum(aList):
    sum=0
    for i in aList:
        if(type(i)==int or type(i)==float):
            sum+=i
    return sum
print(numericSum(["Hello",5,6.1,"Apple"]))
#p8
'''Write a function print reverse(s) that takes a string and prints each character
in reverse order, starting from the last character and ending with the first. For example
print_reverse (" test ")
should print t, s, e,t in that order'''
def printReverse(string):
    string1=""
    for i in range(1, len(string) + 1):
        string1+=string[-i]
    print(string1)

printReverse("hello")

#p9
'''
Write a function named longest string(a list) that takes a list of strings as
input and returns the longest string from the list. If there are multiple strings of the same
length, return the one that appears first. For example
longest_string ([" Python ", "is", "so", "fun ", "and ", " awesome "])
should return “awesome”.'''
def longestString(alist):
    maxa=0
    for i in range(0,len(alist)):
        if len(alist[-i]) > len(alist[maxa]):
          maxa=-i
    return alist[maxa]

print(f"the longest string is{longestString([ "Python ", "is", "so", "fun ", "and ", " awesome "])}")
#p10
'''
. Write a function substring(s, start, end) that takes a string s and two
indices start and end, and returns the substring of s from index start to end (inclusive).
For example
substrings ("Python is awesome ", 1 , 10)
should return “ython is '''
def substring(s,start,end):
        return s[start:end+1]
print(substring("Python is awesome ", 1 , 10))

#p11
'''
Write a function remove first and last(s) that takes a string s and returns
a new string with the first and last characters removed. For example
remove_first_and_last (" banana ")
should return “anan”. Recall that we can use a negative index to slice a string.'''
def removeFirstAndLast(n):
    return n[1:len(n)-1]
print(f"the string with the first and Last letters removed is {removeFirstAndLast("banana")}")
#p12
'''Write a program that asks a user for their name and then prints the first
letter of their name.'''
name=input("whats your name?")
print(f"the first letter of your name is {name[0]}")
#p13
'''
 Write a function called middle character(s) that returns the middle character(s) of the string s. If the length of s is odd, return the middle character. If the length
of s is even, return the two middle characters.
For example:
middle_character ("mango")
should return ‘n’ and
middle_character ("orange")
should return ‘an’.'''
def middleCharacter(n):
    middle=int(len(n) / 2)
    if len(n)%2==0:

        return n[middle-1]+n[middle]
    else :
        return n[middle]
print(f"the middle letter of the word is {middleCharacter("mango")}")
print(f"the middle letter of the word is {middleCharacter("orange")}")
#p14
'''
Write a function find index(a string, char) that returns the index of the last
occurrence of char in the string a string. For example, find index(“banana”, “a”) should
return 5.'''
def findIndex(alist,char):
    for i in range(0,len(alist)):
        if(alist[-i]==char):
            print(alist[i])
            return i

print(f"the index of the char in the word is {findIndex("banana","a")}")
#p15
'''
Write a function called name end with y(a list) that takes a list of names
as input and returns the number of names that end with the letter y.
For example called name end with y([‘Jenny’, ‘John’, ‘Amy’]) should return 2'''
def endWithY(alist):
    count=0
    for i in alist:
        if i[-1]=="y":
            count+=1
    return count

print(endWithY(["Jenny","John","Amy"]))
#P16
'''Create a function named count that accepts a string and a letter as arguments, then returns the count of that letter in the string. For example, if the function call
was count(“banana”, “a”) it would return 3
'''
def countLetter(aString,char):
    count=0
    for i in aString:
        if i==char:
            count+=1
    return count
print("the number of leters in the word is",countLetter("banana","a"))
#p17
'''Write a function num digits(n) that will return the number of digits in an
integer n. Hint: Convert n into a string.
'''
def numDigits(n):
   return len(str(n))
print("the number of digits in the number is",numDigits(183173123718273))
#p18
'''Write a Python function sum of digits(n) that takes an integer n and returns
the sum of its digits. For example, sum of digits(132) should return 6.
'''
def sumOfDigits(n):
    suma=0
    for i in range(0,len(str(n))):
        temp= str(n)
        suma+=int(temp[i])
    return suma

print("the sum of the digits is",sumOfDigits(132))

#p19
'''
(1) Given area code = 60045, format it as “area code: 60045”.
(2) Given invoice number = 3456, format it with the prefix ”INV-” so it appears as
”INV-3456”.
(3) Given name =“John Doe” and title = “Dr.”, format it as “Dr. John Doe”.'''
areaCode=60045
print(f"Area Code: {areaCode}")
invoiceNumber = 3456
print(f"INV-{invoiceNumber}")
name ="John Doe"
title="Dr"
print(f"{title}. {name}")
#p20
'''A palindrome word is a word that reads the same forwards and backward.
For example, “radar”, “level”, “Dad” are palindrome while “hello” is not. Write a program
that takes a word and check if it is a palindrome. Note that “Dad” works because we don’t
distinguish between uppercase and lowercase characters.
'''
def checkPalindrome(aString):
    rString=""
    for i in range(1,len(aString)+1):
        rString+=aString[-i]
    if aString.lower()==rString.lower():
        return True
    else:
        return False


