#P1
'''Define two variables x and y, with values 30 and 7. Calculate their sum,
difference, product, quotient, and integer quotient. Assign these results to new variables
and print them.'''
import math
from pickle import FLOAT

from In_Class.InClassWeek5 import blist

x=30
y=7
suma=30+7
difference=30-7
product=30*7
quotient=30/7
intQuotient=30//7

print(sum,difference,product,quotient,intQuotient)
#p2
'''Write a Python program to ask the user to enter their full name. Based on
their answer, print out their first name.'''
print(input("what is your full name?".split()[0]))
#p3
alist=[int(input("Please enter 1 number")), int(input("please enter another number"))]

if alist[0]>alist[-1]:
    print(alist[0])
else:
    print(alist[-1])
#p4
'''. Alex is shopping for a new pair of shoes. The store has a special discount
offer:
• If the total purchase amount exceeds $100, she gets a 10% discount on the entire
amount.
• If the total purchase amount is between 60 and 100, she gets a 5 % discount.
• If the total purchase amount is less than 60, there is no discount.
Assign a variable to the total purchase that Samantha made. Write a program to calculate
her final payment'''

purchasePrice=float(input("how much did samantha spend"))
if purchasePrice>100:
    rPrice=purchasePrice-(purchasePrice*0.10)
elif(purchasePrice>60):
    rPrice=purchasePrice-(purchasePrice*0.05)
else:
    rPrice=purchasePrice
print(round(rPrice,2))
#p5
'''
Write a program that asks a user for their age and then determines the price
of a movie ticket. The program should print the ticket price according to the following
rules:
• If the user is 12 years old or younger, the ticket price is $8.
• If the user is between 13 and 59 years old, the ticket price is $12.
• If the user is 60 years old or older, the ticket price is $7.'''
age=int(input("Enter your age"))
if(age>=60):
    print("$7")
elif(age>=13):
    print("$12")
else :
    print("$8")
#p7
'''On a piano, a key has a frequency, let’s say f = 400 Hz. Each subsequent
key, whether black or white, has a frequency calculated as f ∗ r^n
, where n is the number
of keys away from the starting key, and r = 21/12. Write a function calc freq(n) that takes
the distance n as an input and returns the frequency of the corresponding key rounded to
the nearest integer'''

def frequency(n):
    return round(400*(2**(1/12))**n)
print(frequency(10))

#P7
'''Write a function named calc dollars(nickel, dime, quarter) that takes three
input values representing the number of nickels, dimes, and quarters, and returns the total
1
amount of money in cents. Here, 1 nickel = 5 cents, 1 dime = 10 cents, and 1 quarter =
25 cents. For example
calc_dollars (1 , 1 , 0)
should return 5 + 10 = 15'''
def calcDollars(nickle,dime,quarter):
    return (nickle*5)+(dime*10)+(quarter*25)
#p8
'''Write a function named simple calculator(num1, num2, operator) that takes
two numbers and a mathematical operator (+, -, *, or /) as inputs. The function should
perform the corresponding operation (addition, subtraction, multiplication, or division)
and return the result. If an invalid operator is provided, the function should return None.
For example'''
def simpleCalculator(num1,num2,operator):
    if(operator=="*"):
        return num1*num2
    elif(operator=="/"):
        return num1/num2
    elif(operator=="+"):
        return num1+num2
    elif(operator=="-"):
        return num1-num2
    return None

#p9
def firstThreeChar(aString):
    return aString[0:3]
print(firstThreeChar("hi"))

#p10
'''Write a function named concat strings(s1, s2) that takes two strings, s1 and
s2, as input. The function should return a new string that concatenates the two strings,
placing the longer string first. If both strings have the same length, return them in the
order they were provided. For example
concat_strings (" apple ", " banana ")
should return “bananapple” and
'''

def concatString(s1,s2):
    return s1+s2
#p11
def countVowels(aList):
    vowels=["a","e","i","o","u"]
    count=0
    for i in aList:
        for j in vowels:
            if i==j:
                count+=1
    return count

print(countVowels("apple"))
#p12
def removeSpaces(aString):
    newString=""
    for i in aString:
        if i!=" ":
            newString+=i
    return newString
print(removeSpaces("    hello World    "))
#p13
def buildSentence(Alist):
    blist=""
    for i in Alist:
        blist+= " "+i

    return blist
print(buildSentence(["hello","I","am","bob"]))
#p14
def findAverage(Alist):
    suma=0
    for i in Alist:
        suma+=i
    return suma/len(Alist)

#p15
def powerList(Alist,n):
    blist=[]
    for i in Alist:
        blist.append(i**n)
    return blist
#p16
def productOfNotOccurences(n,no):
    producta=1
    for i in n:
        if i!=no:
            producta*=i
    return producta

print(productOfNotOccurences([1 , 2 , 3 , 4 , 2] , 2))
#p17
def countWords(sentence):
    blist=[]
    for i in sentence:
        blist=sentence.split()
    return len(blist)
print(countWords("Hello i am bob"))
#p18
fullName=input("Please enter your Full Name: ")
firstName=fullName.split()[0]
print(f"hello {firstName}. How are you doing today?")
#p19
def reverseStrings(Alist):
    bList=""
    for i in range(1,len(Alist)+1):
        bList+=Alist[-i]
    return bList
print(reverseStrings("hello"))
#p20
def sumOfPositives(Alist):
    Suma=0
    for i in Alist:
        if i>0:
            Suma+=i
    return Suma
print(sumOfPositives([-1,2,3,4,5,6,7]))
#p21
def countLessThanEle(n, ele):
    count=0
    for i in n:
        if i <ele:
            count+=1
    return count
print(countLessThanEle([1 , 2 , 3 , 4 , 5] ,3))
listOfStrings=["apple","banana","cherry"]
print([len(i) for i in listOfStrings])
print([i for i in [1, 2, 4, 5, 10] if i%2==0])
import math
print([round(math.sqrt(i),1) for i in [4, 9,
-1, 16, 25, -4] if i >0])



def findMedian(Alist):
    i=0
    middle=int(len(Alist) / 2)
    while i<len(Alist)-1:
        if Alist[i]>Alist[i+1]:
            temp= Alist[i+1]
            Alist[i+1]=Alist[i]
            Alist[i]=temp
            i=i-i
        else:
            i+=1
    return Alist[middle]

print(findMedian([3 , 1 , 2 , 5 , 4]))

def seqSort(Alist):
    i=0
    while i < len(Alist) - 1:
        if Alist[i] > Alist[i + 1]:
            temp = Alist[i + 1].lower()
            Alist[i + 1] = Alist[i].lower()
            Alist[i] = temp.lower()
            i = 0
        else:
            i += 1
    return Alist
def isAnagram(word1,word2):
    listB=[]
    listC=[]
    i=0
    if len(word1)!=len(word2):
        return False
    for i in range(0,len(word1)):
        listB.append(word1[i].lower())
        listC.append(word2[i].lower())
    listB=seqSort(listB)
    listC=seqSort(listC)
    return listB==listC

print(isAnagram("Listen","Silent"))
