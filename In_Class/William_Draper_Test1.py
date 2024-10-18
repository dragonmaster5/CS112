#Problem 1
#Answer:D
#given that output is line by line
def fred():
    print("Zap")


def jane():
    print("Abc")


jane()
fred()
jane()
#Problem 2
x = 12.1
y = 31.25
average = (12.1 + 31.25) / 2
print(round(average, 1))
#Problem 3
fullName = input("Please Enter Your Full Name: ")
print(f" {fullName.split()[-1]}, {fullName[0]}")


#Problem 4
def calculate_perimeter(length, width):
    return round(2 * (length + width), 1)


print(calculate_perimeter(3.1, 2.15))


#problem 5
def calc_gallons(gas_mileage, distance):
    return round(distance / gas_mileage, 1)


print(calc_gallons(32, 100))


#problem 6
def classify_age(age):
    if age >= 65:
        return "Senior"
    elif age >= 20:
        return "Adult"
    elif age >= 13:
        return "Teenager"
    else:
        return "Child"
print([classify_age(i) for i in range(1,100)])

#problem 7
def sum_multiples_of_five(alist):
    suma = 0
    for i in alist:
        if (i % 5 == 0):
            suma += i
    return suma


print(sum_multiples_of_five([5, 3, 4, 10, 5]))


#problem 8
def replace_a_with_o(s):
    string1 = ""
    for i in s:
        if (i.lower() == "a"):
            string1 += "o"
        else:
            string1 += i
    return string1


print(replace_a_with_o("Aardvark"))
#problem 9
words = ["hello", "world", "python"]
wordsC = [i + i for i in words]
print(wordsC)
numList = [-10, 5, -3, 8, -2, 0, 15, 1]
numList2 = [i for i in numList if i > 0]
numList2.sort()
print(numList2)
#problem 10
'''SOLUTION LACKS THE TIME EFFICIENCY TO PASS 90,000 CHECKS '''
def is_triangle_number(n):
    i=0
    while i<18446744073709551615 and i<n:
            if((i*(i+1))/2==n):
                return True
            i+=1
    return False
print([i for i in range(1,101) if is_triangle_number(i)])
#problem 11:
'''I particularly enjoy list comprehesions because it's something that doesn't exist in java and they make my life quicker. '''

