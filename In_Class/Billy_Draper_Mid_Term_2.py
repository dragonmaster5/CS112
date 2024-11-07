#PROBLEM 1
#Answer: C

print([n**2 for n in range(10) if n%3==0])
#PROBlEM 2
#Answer: B
#PROBLEM 3
#Answer: B
#PROBLEM 4
#ANSWER: B
#PROBLEM 5 you don't need to sort because the numbers would be in ascending order anyway
numbers=[10,23,45,33,50,67,75]
numbers.sort()
numbers=[i for i in numbers if i%5==0]
print(numbers)
#2)
strings=["apple","banana","cherry","fig","grape"]
strings=[x for x in strings if len(x)%2!=0]
print(strings)
#PROBLEM 6
def sort_by_released_year(movies):
    for i in range(len(movies)-1):
        if movies[i][-1]>movies[i+1][-1]:
            temp=movies[i+1]
            movies[i+1]=movies[i]
            movies[i]=temp
            sort_by_released_year(movies)

    return [j[0] for j in movies ]
print(sort_by_released_year([("Titanic",1997),("The Matrix",1999),("Inception",2010),("Avatar",2009)]))
#PROBLEM 7
def count_genre(movies):
    d={}
    j=0
    while j<len(movies):
        if movies[j]["genre"] not in d:
            d[movies[j]["genre"]]=1
        else:
            d[movies[j]["genre"]]+=1
        j+=1
    return d
movies=[{"Name":"Titanic", "genre":"Romance"},{"Name":"Inception", "genre":"Sci-Fi"},
        {"Name":"The Matrix", "genre":"Sci-Fi"},{"Name":"The Notebook", "genre":"Romance"},
        {"Name":"Interstellar", "genre":"Sci-Fi"}]
print(count_genre(movies))
#PROBLEM 8
def a(n):
    if n==0:
        return -1
    if n==1:
        return 1
    return 2*a(n-1)+a(n-1)*a(n-2)
print(a(4))
#2)
def NonRecursive_A(n):
    sequence=[-1,1]
    for i in range(2,n+1):
        sequence.append((2*sequence[i-1]+sequence[i-1]*sequence[i-2]))
    return sequence[n]
print(NonRecursive_A(4))
#PROBLEM 9
Teams={"Galaxy Fc": 45,
       "United Fc":50,
       "Lions Fc":50,
       "Tigers Fc":42,
       "Inter Miami CF":50,
       "Columbus Crew":50,
       "Toronto Fc":38}
def top_Teams(teams):
    return sorted([ i for i,k in teams.items() if k == max(teams.values())])
print(top_Teams(Teams))
#PROBLEM 10
Product=[{"product_name":"Apples", "unit_price":0.5, "Number_of_items": 4},{"product_name":"Milk", "unit_price":1.5, "Number_of_items": 1},
        {"product_name":"Bread", "unit_price":2.0, "Number_of_items": 2},{"product_name":"Eggs", "unit_price":3.0, "Number_of_items": 1},]
def getPrice(products):
    price=0
    for i in products:
        price+=i["unit_price"]*i["Number_of_items"]
    return round(price,2)
print(getPrice(Product))
#PROBLEM 11
def group_By_Ratings(d):
    c={}
    for i,v in d.items():
        if v not in c:
            c[v]=[i]
        else:
            c[v].append(i)
    return c
print(group_By_Ratings({"Pasta Place":4.5,"Burger Barn":4.0,"Sushi Spot":4.5,"Taco Town":3.5,"Pizza Palace":4.0,"Salad Station":3.5}))

class Computer:
    def __init__(self,made,listed_price,year_made):
        self.year_made = year_made
        self.made = made
        self.listed_price = listed_price
    def display_info(self):
        return f"Manufacturer: <{self.made}>, Year Made: <{self.year_made}> "
    def final_price(self):
        if 2024-self.year_made>2:
            return round(self.listed_price - (self.listed_price * 0.15), 2)
        return self.listed_price
computer1= Computer("Acer",2000,2021)
computer2= Computer("Acer",2000,2024)
print(computer1.display_info())
print(computer1.final_price())
print(computer2.display_info())
print(computer2.final_price())
#Problem 13
'''Recursion is probably the hardest topic we covered during the second part of this course. I find class structure and inheritance, most interesting out of all the topics we have covered. '''
