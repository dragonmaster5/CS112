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





