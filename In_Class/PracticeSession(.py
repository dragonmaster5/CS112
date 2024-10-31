class Book:
    def __init__(self, title,author,copies, location):
        self.title=title
        self.author=author
        self.copies=copies
        self.location=location
    def displayInfo(self):
        return f"Title: <{self.title}>, Copies Available: <{self.copies}> "
    def isAvailable(self):
        if self.copies>0:
            return True
        return False
    def borrowBook(self):
        if self.isAvailable():
            self.copies-=1
        else:
            print("this book is not available ")
    def returnBook(self):
        self.copies+=1
    def updateLocation(self, newLocation):
        self.location=newLocation

favoriteBook = Book("Way of Kings","Brandon Sanderson", 10,"Bottom Floor")
print(favoriteBook.displayInfo())
favoriteBook.borrowBook()
print(favoriteBook.copies)
favoriteBook.returnBook()
print(favoriteBook.copies)
favoriteBook.updateLocation("Top Floor")
print(favoriteBook.location)
#p2
def frequentWords(sentence):
    d = {}
    l = sentence.split()
    for i in l:
        if i.lower().strip() not in d:
            d[i.lower().strip()] = 1
        else:
            d[i.lower().strip()] = d[i.lower().strip()] + 1
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
with open("president.txt",'rt') as file:
    content=file.read()
    count=0
    for i in content:
         if i == "p":
            count+=1
    print(count)
    count2=0
    l=content.split()
    for i in l:
        if i=="president":
            count2+=1
    print(count2)
    print(frequentWords(content))
    def groupByLength(names):
        d = {}
        maxa=0
        maxl=[]
        for i in names:
            if len(i) not in d:
                d[len(i)] = [i.strip()]
            else:
                d[len(i)].append(i.strip())
        for item,values in d.items():
            if item > maxa:
                maxa=item
                maxl=values
        return maxl
    print(groupByLength(content.split()))

