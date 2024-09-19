import math
#Problem 1
'''
Write a function called poly perimeter that takes in two parameters, len side,
and num sides, and returns the perimeter of the polygon. The perimeter of a polygon is
the length of each side times the number of sides. For example, poly perimeter(4,5) should
return 20
'''
def polyPerimeter(numSides,lenSide):
    return numSides*lenSide
#Problem 2
'''Create a function called get hypotenuse that takes in two parameters, a and
b, which represent the lengths of the two legs of a right triangle. The function should
return the length of the hypotenuse. Use the Pythagorean theorem'''
def getHypotenous(a,b):
    return math.sqrt(a**2+b**2)

#Problem 3
'''Write a function called find distance that takes in four parameters, x1, y1, x2, y2,
and returns the distance between these two points (x1, y1) and (x2, y2). The distance is
given by the following formula which is a consequence of the Pythagorean theorem'''
def  distance(x1,x2,y1,y2):
    return math.sqrt(((x1-x2)**2)+((y1-y2)**2))
#p4
'''
Write a function called total string length that takes in two parameters, str1
and str2, and returns the total length of these two strings
'''
def  TotalStringLength(str1,str2):
    return len(str1+str2)
#p5
'''
Write a function called address that combines 3 different string address parameters (city, state, and zip) and returns a user’s address. After the city and state inputs,
add a comma and a space.'''
def address(city,state,zipcode):
    return f" {city}, {state},{zipcode}"
#p6
'''
Write a function apply discount(price, is member) that applies a discount
based on membership status:
• 10% discount for members.
• No discount for non-members.
'''
def applyDiscount(price,isMember):
    if(isMember):

        return price-(price*0.1)
    else :
        return price
#p7
'''
Write a function called shipping price that takes two arguments: weight and
express and returns shipping cost based on the weight of the package and whether express
shipping is selected:
1
• Standard Shipping:
– $5 for weights up to 2 lbs
– $10 for weights above 2 lbs
• Express Shipping:
– $10 for weights up to 2 lbs
– $20 for weights above 2 lbs
'''
def shippingCost(weight,express):
    if(express):
        if(weight<2):
            return 5
        else :
            return 10
    else :
        if (weight < 2):
            return 10
        else:
            return 20
#p8
'''
Write a function called final price that takes three arguments: price, weight,
and express and returns the final total price. The final price is the sum of the price and
the shipping cost which is calculated as follows
• For purchase prices $100 or more, shipping is free.
• For purchase prices below $100, the shipping fee is calculated based on the formula
from the previous problem.
Your function should call the shipping price from the previous problem.
'''
def finalPrice(price,weight,express):
    if(price>=100):
        return 0
    else:
        return shippingCost(weight,express)
#p9
'''
 Write a function countdown to zero(start) that counts down from the given
start number to 0, printing each number. If the starting number is less than or equal to 0,
the function should print a message “Enter a positive number”.
'''
def countDownToFinal(start):
    if(start>0):
        while(start>0):
            print(start)
            start-=1
    else:
        print("please enter a postitive number")

countDownToFinal(10)

#p10
'''Write a function buzz(n) that prints the numbers from 1 to n. For multiples
of 3, print “Buzz” instead of the number.
'''
def Buzz(n):
    for i in range(1,n+1):
        if(i%3==0):
            print("Buzz")
        else:
            print(i)
print(Buzz(10))
#p11
'''
Write a function called negative sum(a list) that takes a list as an input.
The function will return the sum of all negative numbers in the list
'''
def negativeSum(aList):
    suma=0
    for i in aList:
        if i<0:
            suma+=i
    return suma
print(negativeSum([-10,20,30,50,-20]))
#p12`
'''
Write a function called even positive sum(a list) that takes a list of integers
as an input. The function will return the sum of all positive even numbers in the list (a
positive even number is a number that is both positive and even). 
'''
def evenPositiveSum(aList):
    suma=0
    for i in aList:
        if i>0 and i%2==0:
            suma+=i
    return  suma
#p13
'''
Write a function called maximal element(a list) that takes a list as an input.
The function will return the maximal element in the list. 
'''
def Maximum(aList):
    maxi=0
    for i in aList:
        if(i>maxi):
            maxi=i
    return maxi
#p14
'''Write a function called is prime(n) that checks whether a number is a prime
number or not. A prime number is a number whose divisors are 1 and itself. For example:
2, 5, 7, and 11 are prime numbers while 6 is not.'''
def isPrime(n):
    num=n

    while n>1 :

        if num%n==0:
            return False
        n-=1
    return True
print(isPrime(2))
print(isPrime(6))

#p15
'''
Write a function called sum divisors(n) that calculates the sum of all of the
divisors of n.
'''
def sumOfDivsors(n):
    suma=0
    divisor=n
    while n>0:
        if divisor%n==0:
            suma+=n
        n-=1
    return suma
print(sumOfDivsors(10))
#p16
'''
Write a function called sum square(n) that calculates the sum of the squares
of all numbers between 1 and n. For example, sum square(1) should return 1 and sum square(2)
should return 5.
'''
def sumOfSquares(n):
    if n==0:
        return n
    else :
        return math.sqrt(n)+math.sqrt(sumOfDivsors(n-1))
print(sumOfSquares(5))
#p17
'''
An integer n is called a perfect square if n = m2
for some integer n. For
example, 4 is a perfect square because 4 = 22
. On other other hand, 6 is not a perfect
square. Write a function called is square(n) to check whether a number n is a perfect
square.
'''
def isSquare(n):
    return math.sqrt(n)>1 and math.sqrt(n)==int(math.sqrt(n))

#p18
'''
Write a function that prints out all perfect square numbers between 1 and
100.
'''
def perfectSquare():
     i=0
     while i<100:
        if isSquare(i):
            print(i)
        i+=1
#p19
'''
Write a function that takes a string as an input and returns True if this
string contains the lowercase letter h. Otherwise, return False.
'''
def isLowerCaseH(n):
    for i in n:
        if(i=="h"):
            return True
    return False
print(isLowerCaseH("happy"))
print(isLowerCaseH("sad"))