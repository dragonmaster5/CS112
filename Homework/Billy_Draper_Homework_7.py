#P1
'''Given a list of words, create a new list containing the first letter of each word. For
example, for the list
words = [" apple ", " banana ", " cherry "]
the output should be
["a", "b", "c"]
(2) Given a list of words, create a new list that contains only the words that start with
a vowel (a, e, i, o, u). For example, for the list
words = [" apple ", " banana ", " orange ", " grape ", " umbrella "]
the output should be
[" apple ", " orange ", " umbrella "]
'''
from pickle import TUPLE

#1)
firstLetter = [i[0] for i in ["apple", "banana", "cherry"]]
print(firstLetter)
#2)
containsVowel = [i for i in ["apple", "banana", "orange", "grape", "umbrella"] if i[0] in 'aeiou']
print(containsVowel)
#p2
'''Given a list of tuples, create a new list containing the second element from each
tuple. For example
tuples = [(1 , "a") , (2 , "b") , (3 , "c") ]
the output should be
["a", "b", "c"]
(2) Given a list of tuples where the first element is a number, create a new list that includes only those tuples where the first element is greater than a specified threshold
value. For example
'''
#1)
secondElement = [i[-1] for i in [(1, "a"), (2, "b"), (3, "c")]]
print(secondElement)
#2)
threshold = 2
greaterThanThreshold = [i for i in [(1, "a"), (3, "b"), (5, "c")] if i[0] > threshold]
print(greaterThanThreshold)
#p3
'''(1) Problem: Create a tuple containing the names of four of your favorite fruits. For
me, it is
favorite_fruits = (" mango ", " pear ", " grape ", " cherry ")
(2) Print out the first and last elements of your tuple.
(3) Add a new fruit to this tuple.
(4) With this updated tuple, create a list of fruits whose names have at least 5 characters. You can use the append method and/or list comprehension for this problem.
'''
#1)
favoriteFruits = ("cantaloupe", "strawberry", "peach", "apple", "pear")
print(favoriteFruits)
#2)
print(favoriteFruits[0], favoriteFruits[-1])
#3)
favoriteFruits += ("mango",)
#4
favoriteFruitsList = []
for i in favoriteFruits:
    if len(i) >= 5:
        favoriteFruitsList.append(i)
print(favoriteFruitsList)
#p4
'''4. Write a function named flatten tup(nested tuple) that takes a nested tuple
as input and returns a single flattened tuple. For example
nested_tuples = ((1 , 2) , (3 , 4) , (5 , 6) )
flatten_tup ( nested_tuples )
should return
(1 ,2 ,3 ,4 ,5 ,6)
For this problem, you need to initiate an empty tuple before the for loop and keep
updating this tuple. To create an empty tuple, you can use the syntax
new_tup = ()'''


def flattenTup(nestedTup):
    emptyTuple = ()
    for i in nestedTup:
        if isinstance(i, tuple):
            for j in i:
                emptyTuple += (j,)
    return emptyTuple


print(flattenTup(((1, 2), (3, 4), (5, 6))))
#p5
'''Let us consider the following dictionary
state_capitals = {
" Illinois ": " Springfield ",
" California ": " Sacramento ",
" Texas ": " Austin ",
"New York ": " Albany ",
" Florida ": " Tallahassee "
}
In this dictionary, each key represents a state, and the corresponding value is its capital.
(1) For each state in the dictionary, print out a sentence in the format: “The capital
of Illinois is Springfield”.
(2) Add the key-value pair ”Wisconsin”:“Madison” to this dictionary.
(3) Using the updated dictionary, create a list of states whose capital names start with
the letter A.
2'''
#1)
state_capitals = {
    " Illinois ": "Springfield ",
    " California ": "Sacramento ",
    " Texas ": "Austin ",
    "New York ": "Albany ",
    " Florida ": "Tallahassee "
}
for i in state_capitals.keys():
    print(f"the capital of {i} is {state_capitals[i]}")
#2)
state_capitals.update({"Wisconsin": "Madison"})
#3)
print([i for i in state_capitals.keys() if state_capitals[i][0].lower() == "a"])
#p6
'''Write a function named get average score(student grades) that takes in a dictionary student grades(d) as input and returns a new dictionary containing each student”s
name and their average score rounded to the one decimal place. Here student grades is
a dictionary whose each key is a student”s name and the corresponding value is a list of
student”s scores throughout the semester.
For example
student_grades = {
" Benjamin ": [56 , 79 , 90 , 22 , 50] ,
" David ": [88 , 62 , 68 , 75 , 78] ,
" Becky ": [95 , 88 , 92 , 85 , 85] ,
" Anne ": [76 , 88 , 85 , 82 , 90] ,
" Isis ": [99 , 92 , 95 , 89 , 99]
}
get_average_score ( student_grades )
should return
{" Benjamin ": 59.4 , " David ": 74.2 ,
" Becky ": 89.0 , " Anne ": 84.2 , " Isis ": 94.8}
For this problem, you can use the sum/max/min/len etc methods for a list.'''


def averageScore(studentGrades):
    averageGrade = {}
    for i in studentGrades.keys():
        avg = round(sum(studentGrades[i]) / len(studentGrades[i]), 1)
        averageGrade.update({i: avg})
    return averageGrade


print(averageScore({
    " Benjamin ": [56, 79, 90, 22, 50],
    " David ": [88, 62, 68, 75, 78],
    " Becky ": [95, 88, 92, 85, 85],
    " Anne ": [76, 88, 85, 82, 90],
    " Isis ": [99, 92, 95, 89, 99]
}))

#p7 Only overengineered this problem slightly
'''Write a function named highest rating(books and ratings) that takes a dictionary books and ratings as input and returns the list of books that have the highest rating.
The dictionary books and ratings contains the titles of books and their corresponding ratings on a scale from 1-5. For example
books_and_ratings = {
" Siddhartha ": 4.8 ,
" 1984 ": 4.8 ,
"To Kill a Mockingbird ": 4.7 ,
" Pride and Prejudice ": 4.6 ,
"The Great Gatsby ": 4.8
}
print ( highest_rating ( books_and_ratings ) )
should return
[ " Siddhartha ", "The Great Gatsby "]
'''


def highestRatings(booksAndRatings):
    keyList = []
    highestRating = []
    iDict={}
    for i in booksAndRatings:
        keyList.append((i,booksAndRatings[i]))
    for j in range(0, len(keyList)-1):
        if keyList[j][-1] > keyList[j+1][-1]:
            temp =keyList[j+1]
            keyList[j+1]=keyList[j]
            keyList[j]=temp
            for k in keyList:
                iDict.update({k[0]:k[-1]})
            highestRatings(iDict)
    for k in booksAndRatings.keys():
        if booksAndRatings[k] == keyList[-1][-1] :
            highestRating.append(k)
    return highestRating


print(highestRatings({
    " Siddhartha ": 4.8,
    " 1984 ": 4.8,
    "To Kill a Mockingbird ": 4.7,
    " Pride and Prejudice ": 4.6,
    "The Great Gatsby ": 4.8
}))
#p8
'''Let”s imagine that you manage a small online store and want to analyze
the sales data for three products: Wireless Headphones, Bluetooth speakers, and Smartwatches. The data is recorded using the following format
3
sales = {
" Wireless Headphones ": [120 , 150 , 130] ,
" Bluetooth Speaker ": [80 , 90] ,
" Smartwatch ": [200 , 250 , 300]
}
Write a function named sale summary(sales) that returns a list summarizing the total sales
and the number of sales recorded for each product. For the above example, your function
should return
[{" product ": " Wireless Headphones ", " total_sales ": 400 , " count ":
3} ,
{" product ": " Bluetooth Speaker ", " total_sales ": 170 , " count ": 2} ,
{" product ": " Smartwatch ", " total_sales ": 750 , " count ": 3}]'''

def saleSummary(sales):
    salesList=[]
    for i in sales.keys():
        tempDict={"product":i, "TotalSales":sum(sales[i]), "count":len(sales[i])}
        salesList.append(tempDict)

    return salesList
print(saleSummary({
" Wireless Headphones ": [120 , 150 , 130] ,
" Bluetooth Speaker ": [80 , 90] ,
" Smartwatch ": [200 , 250 , 300]
}))
#p9
'''Write a function named convert to F(temps celsius) that takes a dictionary
of cities and their temperatures in Celsius as input and returns a new dictionary whose keys
are the same but whose values are the corresponding temperature in Fahrenheit (rounded
to one decimal place). For example
temps_celsius = {" Madison ": 14 , " Hanoi ": 25 , " Chicago ": 15}
convert_to_F ( temps_celsius )
should return
{" Madison ": 57.2 , " Hanoi ": 77.0 , " Chicago ": 59.0}'''
def convertToF(tempsC):
    for i in tempsC.keys():
        tempsC[i]=(tempsC[i]*(9/5))+32
    return tempsC
print(convertToF({" Madison ": 14 , " Hanoi ": 25 , " Chicago ": 15}))
#p10
'''Given a dictionary where the keys are student names and the values are
their scores, write a function named convert to letter grades(scores) that converts each
score to a letter grade based on the following scale:
• A: 90 - 100
• B: 80 - 89
• C: 70 - 79
• D: 60 - 69
• F: 0 - 59
For example
scores = {" Alice ": 95 , "Bob ": 82 , " Charlie ": 88 , " Diana ": 100}
convert_to_letter_grades ( scores )
should return
4
{" Alice ": "A", "Bob": "B", " Charlie ": "B", " Diana ": "A"}
For this problem, it is a good idea to write a separate function named to letter(a score)
that converts a score to a letter grade. For example
to_letter (93)
should return ”A”. You can then call this new function inside convert to letter grades(scores).
Doing so would make your function easier to read/debug'''

def covertToLetterGrades(Scores):
    def toLetter(num):
        if num >= 90 <= 100:
            return "A"
        elif num >= 80:
            return "B"
        elif num >= 70:
            return "C"
        elif num >= 60:
            return "D"
        else:
            return "F"
    for i in Scores.keys():
        Scores[i]=toLetter(Scores[i])
    return Scores
print(covertToLetterGrades({" Alice ": 95 , "Bob ": 82 , " Charlie ": 88 , " Diana ": 100}))
