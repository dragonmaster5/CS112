#p1
'''Create a function called sales tax(list of costs) that takes in a list of costs
(floating point values) as a parameter and returns a dictionary with the original costs as
keys and the final costs after the sales tax of 6 percent as values. The final costs should
be rounded to the hundredth place. For example,
sales_tax ([1.25 , 8 , 5])
returns
{1.25: 1.33 , 8: 8.48 , 5: 5.3}.'''
from tkinter.font import names


def salesTax(aList):
    SaxDict = {}
    for i in aList:
        salesT = i * 0.06
        SaxDict.update({i: round(i + salesT, 2)})
    return SaxDict


print(salesTax([1.25, 8, 5]))
#p2
'''2. Write a function named triple values(num list) that takes in a list of numbers,
num list, which adds every number in the list to a dictionary as the key and adds three
times the number as the value. Then, change every even value (not the keys) in the
dictionary to zero. For example, triple values([1, 2]) should return {1: 3, 2: 0 }'''


def tripleValues(numList):
    tripDict = {}
    for i in numList:
        tripDict.update({i: i * 3})
    for i, y in tripDict.items():
        if y % 2 == 0:
            tripDict[i] = 0
    return tripDict


print(tripleValues([1, 2]))
#p3
'''Write a function named count chars(str1) that takes a string, str1, and returns
a list of tuples. Each tuple should consist of a character from the string and the number
of times it appears. The characters should be keys, and their frequencies should be the
values. For example
count_chars ("babby")
should return
[("b": 3) , ("a" :1) , ("y": 1)'''


def seqSort(l):
    for i in range(0, len(l) - 1):
        if l[i][-1] > l[i + 1][-1]:
            temp = l[i + 1]
            l[i + 1] = l[i]
            l[i] = temp
            seqSort(l)
    return l


def countChars(str1):
    charDict = {}
    l = []
    for i in str1:
        if i not in charDict:
            charDict[i] = 1
        else:
            charDict[i] = charDict[i] + 1
    for char, num in charDict.items():
        l.append((char, num))

    return seqSort(l)


print(countChars("babby"))

#p4
'''Write a function letter dict(s) that takes in a string s as a parameter and
returns a dictionary containing the amount of times letters appear in the given string. For
example,
letter_dict ("It is")
should return
{"i": 2 , "t": 1 , "s": 1}.'''


def letterDict(s):
    charDict = {}
    for i in s:
        if i != " ":
            if i.lower() not in charDict:
                charDict[i.lower()] = 1
            else:
                charDict[i] = charDict[i] + 1
    return charDict


print(letterDict("It is"))
#p5
'''. Write a function most frequent words(sentence) that takes in a sentence as
a parameter and returns a list of the most common words in this sentence. For example,
most_frequent_words ("The cat sat on the mat , and the cat was happy
")
should return
["the"]
For this problem, we assume that the sentence string doesn’t have any punctuation
besides spaces.'''


def frequentWords(sentence):
    d = {}
    l = sentence.split()
    for i in l:
        if i.lower() not in d:
            d[i.lower()] = 1
        else:
            d[i.lower()] = d[i.lower()] + 1
    l = []
    maxa = ("", 0)
    for word, count in d.items():
        l.append((word, count))
        if count > maxa[-1]:
            maxa = (word, count)
    for i in range(0, len(l)):
        temp = l.pop(0)
        if temp[-1] == maxa[-1]:
            l.append(temp[0])
    return l


print(frequentWords("The cat sat on the mat , and the cat was happy hi hi hi"))
#p6
'''. Write a function repeated numbers(alist) that takes alist of numbers and
returns a new list containing the numbers that appear at least three times in the original
list. For example
repeated_numbers ([4 , 2 , 3 , 2 , 4 , 4 , 1 , 3 , 3 , 5 , 2])
should return
[4 , 2 , 3]'''


def repeatedNumbers(aList):
    d = {}
    for i in aList:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1


    return [num for num,count in d.items() if(count>3)]


print(repeatedNumbers([4, 2, 3, 2, 4, 4, 1, 3, 3, 5, 2]))
#p7
'''Write a function called group by length(names) that takes a list of names as
input and returns a dictionary where the keys represent the lengths of the names, and the
values are lists of names that have that specific length. For example
group_by_length ([" Alice ", "Bob", " Charlie ", " David ", "Eve", " Frank
"])
should return
{3: ["Bob", "Eve"] , 5: [" Alice ", " David "] , 7: [" Charlie "] , 5: ["
Frank "]}'''


def groupByLength(names):
    d = {}
    for i in names:
        if len(i) not in d:
            d[len(i)] = [i]
        else:
            d[len(i)].append(i)
    return d


print(groupByLength(["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]))
#p8
'''Write a function named group by age(d) that takes a dictionary d as input,
where the keys are names and the values are ages. The function should return a new
dictionary where the keys are ages, and the values are lists of names of people who have
that age. For example
d = {
" Alice ": 30 ,
"Bob": 25 ,
" Charlie ": 30 ,
" David ": 25 ,
"Eve": 30
}
group_by_age ( d )
should return
{30: [" Alice ", " Charlie ", "Eve "] ,
25: ["Bob", " David "]}
'''


def groupByAge(d):
    l = []
    for name, age in d.items():
        l.append((name, age))
    d = {}
    for i in range(0, len(l)):
        if l[i][-1] not in d:
            d[l[i][-1]] = [l[i][0]]
        else:
            d[l[i][-1]].append(l[i][0])
    return d


print(groupByAge({
    " Alice ": 30,
    "Bob": 25,
    " Charlie ": 30,
    " David ": 25,
    "Eve": 30
}))
#p9
'''. Given the following nested dictionaries. In this dictionary, each key is a
student’s name and the value is another dictionary containing the student’s courses in a
semester along with their corresponding scores
students = {
" Alice ": {" Math ": 90 , "CS": 85 , " Physics ": 80} ,
"Bob": {" Math ": 78 , "CS": 92 , " Chemistry ": 88} ,
" Charlie ": {"CS": 95 , " Neuroscience ": 92 , " Data Science ": 91} ,
" David ": {" Math ": 85 , " Physics ": 90 , " Chemistry ": 80} ,
"Eve": {" Neuroscience ": 91 , " Data Science ": 87 , " Physics ": 88}
}
(1) Find Alice’s grade for Math.
(2) Find the list of students who take CS.
(3) Find the student with the highest score in Neuroscience'''
#(1)
students = {
    " Alice ": {" Math ": 90, "CS": 85, " Physics ": 80},
    "Bob": {" Math ": 78, "CS": 92, " Chemistry ": 88},
    " Charlie ": {"CS": 95, " Neuroscience ": 92, " Data Science ": 91},
    " David ": {" Math ": 85, " Physics ": 90, " Chemistry ": 80},
    "Eve": {" Neuroscience ": 91, " Data Science ": 87, " Physics ": 88}
}
print(students[" Alice "][" Math "])
#(2)
maths = []
for i in students.keys():
    if "CS" in students[i]:
        maths.append(i)
print(maths)


#(3)
def highestScore(d):
    maxa = ("", 0)
    for k in d.keys():
        if " Neuroscience " in d[k]:
            if d[k][" Neuroscience "] > maxa[-1]:
                maxa = (k, d[k][" Neuroscience "])
    return maxa


print(highestScore(students))
