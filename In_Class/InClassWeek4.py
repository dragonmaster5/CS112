#p1
#C
from Workspace import my_list

#p2
#Pym, answer E

Mylist=["cs","math","chemistry"]
n=len(Mylist)
myRange=range(1,n+1)
for i in myRange:
    print(Mylist[-i])
aList=[0,-1,-3,4,6]
suma=0
for i in aList:
    suma+=1

print(suma)


firstNames= ["Armin","Karli","nacho","Ayush","Kyla"]
for i in firstNames:
    if i[0].lower()=="a":
        print(i)

first_names= ["Grisha","Miley","Ian","Samra","Kyla"]
for name in first_names:
    for letter in name:
        if letter.lower()=="y":
            print(name)

numList=[1,2,3,4]
for i in range(len(numList)):
    numList.append(numList.pop(i)*2)

print(numList)

evenList=[0,-1,2,2,1]
list2=[]
for i in evenList:
    if(i%2==0):
        list2.append(i)

print(list2)

list2=[]
a_list=["dad","mom","a","apple","hello","Bob"]
for i in a_list:
    if i[0]==i[-1] and len(i)>1:
        list2.append(i)
print(list2)


def addlists(alist,blist):
    nlist=alist+blist
    print(nlist)
    for j in range(-1,len(nlist)):
        if nlist[j]>nlist[j+1]: #checks if bounds at index i is greater than bounds at index i + 1
            temp=alist[j+1] #if true it sets a temporary variable = to bounds at index i+1
            nlist[j+1]=nlist[j] # then sets bounds i to bounds i + 1  and bounds i to temp
            nlist[j]=temp
            j=j-j #resets the sequence to check if the previous number is bigger as well, i know it's not most efficient way to do that
        else :
            j+=1# moves to the next index in the loop
        print(j)
    return alist


print(addlists([-1,2,3],[2,-3,4]))


full_names= "Billy Draper"
print(full_names.split()[-1])

sentence=input("please enter a sentence")
print(sentence.split()[-1])
old_list=[1,4,7,8]
print([str(i) for i in old_list])

print([i[0] for i in ["Andrew","Louis","Samra","Maya"]])
def doubleString(s):
    return s+s
print([doubleString(i) for i in ["a","b","c","d"]])
def cToF(n):
    return round((9/5*n)+32,2)
print([cToF(i) for i in [0,20,37,100]])

print([item for item in ["Grisha","Maya","Ian","Colin"] if item[-1].lower()=="a"])
def sumOfDigits(n): #sorry saw a recursive solution, had to try it.
    if n==0:
        return n
    return int(n%10+sumOfDigits(n/10))

print(sumOfDigits(132))