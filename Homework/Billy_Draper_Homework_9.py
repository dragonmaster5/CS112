import numpy as np
import matplotlib.pyplot as plt
#Problem 1
'''Problem 1. Given the following sets
s1 = {1 , 2 , 3 , 4 , -2 , -3}
s2 ={1 , 2 , 5 , 7}
Do the following tasks.
(1) Add 5 and 6 to s1.
(2) Find the union of s1 and s2.
(3) Find the number of elements that belong to both s1 and s2.
(4) Find the list of elements that belong to s1 but not s2.'''
s1={1,2,3,4,-2,-3}
s2={1,2,5,7}
s1.update([5,6])
s3=s1.union(s2)
print(s1)
print(s3)
inS1= len(s1.intersection(s2))
print(inS1)
print(len([i for i in s1 if i not in s2]))
#P2
'''In a school, students are enrolled in different courses. The sets A and B
represent students enrolled in Mathematics and Physics courses, respectively:
A = {" John ", " Sarah ", " Mike ", " Anna ", " David "}
B = {" Sarah ", " Mike ", " David ", " Alice "}
(1) Find the set of students who are enrolled in both Mathematics and Physics.
(2) Find the set of students who are enrolled in either Mathematics or Physics.
(3) How many students are enrolled in Mathematics but not in Physics?
(4) Find the list of students who are enrolled in only one of the two courses.
'''
A = {" John ", " Sarah ", " Mike ", " Anna ", " David "}
B = {" Sarah ", " Mike ", " David ", " Alice "}
#1)
aIn=A.intersection(B)
print(aIn)
#2)
inBoth=A.union(B)
print(inBoth)
#3)
howManyInMath=len(A)
print(howManyInMath)
#4)
enrolledInOn= A-B | B-A
print(enrolledInOn)
#problem 3
'''(1) Create a numpy array with integers from 1 to 10 (inclusive).
(2) Create a new array by adding 5 to each element of the original array.
(3) Create another new array by multiplying each element of the original array by 3.
(4) Create a final array by squaring each element of the original array.
'''
#1)
arr= np.linspace(1,10,10)
print(arr)
#2)
add5=arr+5
print(add5)
#3)
mult3=arr*3
print(mult3)
#4)
squaredArr=arr**2
print(squaredArr)
#problem 4
'''Given the following numpy array
my_arr = np . array ([1 , -1 , 3 , 5 , 7 , 12])
(1) Create a numpy array containing the squares of the elements in my arr.
(2) Create a numpy array containing the square roots of the non-negative elements in
my arr (ignore the negative elements). Round the result to 2 decimal places.
1
(3) Create a numpy array containing the exponential of the elements in my arr. Round
the result to 2 decimal places.
(4) Create a numpy array containing the inverse of the elements in my arr. Round the
result to 2 decimal places'''
#1)
my_arr = np . array ([1 , -1 , 3 , 5 , 7 , 12])
my_arrSquared=my_arr**2
print(my_arrSquared)
#2)
my_arrSqrt=np.sqrt(my_arr[my_arr>0]).round(2)
print(my_arrSqrt)
#3)
inverArr=(1/my_arr).round(2)
print(inverArr)
#P5
'''Given the following numpy arrays, where each element represents the radius
and height of a different cylinder.
radii = np . array ([1 , 2.1 , 3 , 4.1])
height = np . array ([3 , 4 , 2.5 , 10])
Create a new array that calculates the volume of the corresponding cylinder. The formula
for the volume is given by
A = πr2h,
where r is the radius and h is the height.
'''
radii = np . array ([1 , 2.1 , 3 , 4.1])
height = np . array ([3 , 4 , 2.5 , 10])
Volume= (np.pi*radii**2)*height
print(Volume)
#P6
'''Given the following numpy array
my_arr = np . array ([1 , 2 , -3 , 4 , 9 , 10])
Use boolean indexing to answer the following questions.
(1) Create a new array that contains only the positive elements from the original array.
(2) Create a new array that contains only the elements that are multiples of 3 from the
original array.'''
#1)
my_arr2 = np . array ([1 , 2 , -3 , 4 , 9 , 10])
posArr= my_arr2[my_arr2>0]
print(posArr)
#2)
mult3Arr= my_arr2[my_arr2%3==0]
print(mult3Arr)
#P7
'''Use the np.linspace() method to plot the graph of the following function over
the interval [0, 2]
'''
plotArr=np.linspace(0,2,100)
graph= (np.e**-plotArr)+3*np.sin(plotArr)
plt.plot(plotArr,graph)
plt.show()

