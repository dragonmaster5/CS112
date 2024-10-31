class Student:
    def __init__(self, name, major, nationality):
        self.name = name
        self.major = major
        self.nationality = nationality


class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def getDescription(self):
        return f"Title:{self.title}, Author: {self.author}, Year Published {self.year_published} "

    def isClassic(self):
        return self.year_published < 2024 - 50

    def __st_(self):
        return f"Title:{self.title}, Author: {self.author}, Year Published {self.year_published} "


favoriteBook = Book("Way of Kings", "Brandon Sanderson", 2010)
print(favoriteBook)


class BankAccount:
    def __init__(self, balance, accountHolder):
        self.balance = balance
        self.accountHolder = accountHolder

    def display_balance(self):
        print(f"Current Balance: \"{self.balance}\", ")

    def deposit(self, amount):
        if amount<0:
            print("Cant deposit a negative number ")
            return
        else:
            self.balance+=amount
            return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance-=amount
            return self.balance


myAccount = BankAccount(10000, "Billy ")
myAccount.display_balance()
myAccount.deposit(125)
print(myAccount.balance)
myAccount.display_balance()
