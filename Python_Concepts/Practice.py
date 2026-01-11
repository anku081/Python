'''def add(a, b):
    print("Addition of a and b: ", a+b)
    return "Printing the result"

def sub(a,b):
    print("Subtraction of a and b: ", a-b)
    return "printing the result"

if __name__ == "__main__":
    a=int(input("enter a: "))
    b=int(input("enter b: "))
    c = lambda x:a**2
    print(add(a, b))
    print(sub(a,b))
    print(c)
'''


'''def condition(a, b):
    if a > b:
        print("this is inside the conditions")
        print("still inside")
    print("This is outsides")


if __name__ == "__main__":
    a=int(input("enter a: "))
    b=int(input("enter b: "))
    print(condition(a, b))'''


'''fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)'''

'''#x= "awesome"

def myfunc():
    global x
    x="Tanu"
    print("Python is "+ x)

myfunc()
print("Python is "+ x)'''

'''x= {"anku", "tanu", "sona"} ## Mutable and unordered data structure that store the data unique.
y = frozenset({"apple", "mango", "cherry"}) ## Imutable and unordered set
print(x, "\n", y)

x.add("raj")
#print(x.pop())
x.remove("tanu")
print(x)'''

'''#Data Types
#1. Numeric Types:
x = int(input("enter a integer variable: "))
y = float(input("enter a float variable: "))
z = complex(input("enter a complex number: "))
a = bool(input("enter a boolean number: "))
print(x, "\n", y, "\n", z, "\n", a)'''

'''fruits = ["apple", "banana", "cherry", "kiwi"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)
newlist = [x for x in fruits if "e" in x]
print(newlist)'''

'''newlist = [x for x in range(20) if x%2 == 0]
print(newlist)'''

'''thisset = {"apple", "banana", "orange"}
for x in thisset:
    print(x)

thisset.add("anku")
print("printing set element", thisset)
print("banana" in thisset)
print("kiwi" not in thisset)

newset = ["sona", "tanu"]
thisset.update(newset)
print(thisset)
#newset.remove("muskan")
thisset.discard("muskan")
print(thisset.pop())'''

'''set1 = {"apple", "banana", "cherry"}
set2 = {1,2,3,4,5}
set3 = set1.intersection(set2)
print(set3)'''


'''x = frozenset({"apple", "banana", "kiwi"})
print(x)
print(type(x))

thisdict = {
    "name": ["anku", "sona", "tanu"],
    "age": [28, 25, 24]
}'''

'''print(thisdict.keys())
print(thisdict.values())
print(thisdict["name"])
print(thisdict["age"])
thisdict["name"][0]="Anku"
print(thisdict.keys())
print(thisdict.values())

for i, j in thisdict.items():
    print(i, j)'''

'''if "name" in thisdict:
    print("yes it is in the values of dictionary")
else:
    print("it isn't present")'''


'''day=int(input("enter day number that you want to know: "))
month = 4
match day:
    case 1 | 2 | 3 | 4 | 5 | 6 if month == 4:
        print("There is working Day in April")
    case 7 | 8 if month == 5:
        print("There is weekend Day in May")
    case _:
        print("There is no match")
'''
'''def my_function(greeting,*a):
    for i in a:
        print(greeting, i)
        

result = my_function("Hello", "Anku", "Tanu", "Sona")
print(result)'''

'''def changecase(func):
    def myinner():
        return func().upper()
    return myinner

def addgreeting(func):
    def myinner():
        return "Hello " + func() +"Have nice day"
    return myinner

@changecase
@addgreeting
def myfunction():
    return "anku love to sona "


@changecase
@addgreeting
def otherfunction():
    return "hello competative programming"

print(myfunction())
print(otherfunction())'''


'''def myfunction():
  return "Have a great day!"

print(myfunction.__name__)
print(myfunction.__doc__)'''

'''x=lambda a, b:a+b+10
print(x(5, 10))'''

'''def myfunction(n):
    return lambda a:a*n

first = myfunction(2)
second = myfunction(5)

print(first(10))
print(second(20))'''
'''
numbers = [1,2,3,4,5]
double = list(map(lambda a:a*2, numbers))
odd_number = list(filter(lambda a:a%2==0, numbers))
print(double)
print(odd_number)'''

'''numbers = [1,2,3,4,5]
myiter = iter(numbers)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))'''



'''import greeting
import datetime
name = ["Anku", "Tanu", "Monu", "Sona", "Annu"]
for i in name:
    print(greeting.greet(i))

x = datetime.datetime.now()
print(x.year)
print(x.month)
print(x.hour)
print(x.minute)'''

'''try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")'''

'''x=-1
if x<0:
    raise Exception("Sorry, no number below zero")'''

'''class student:
    def __init__(self, name, age, clas):
        self.name = name
        self.age = age
        self.clas = clas

    def sum(self):
        return self.age + self.clas
    
    def welcome(self):
        return "Welcome my dear student " + self.name
    
s1 = student("Anku", 27, 15)
s2 = student("Tanu", 23, 14)
s3 = student("sona", 21, 12)

print(s1.name, s1.age, s1.clas)
print(s2.name, s2.age, s2.clas)
print(s3.name, s3.age, s3.clas)
print(s1.sum())
print(s1.welcome())'''

'''class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)'''

'''#Inheritence
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.secondname = lname

    def printname(self):
        print(self.firstname, self.secondname)

x = person("Anku", "Sona")
x.printname()

class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

s1 = student("Tanu", "Kumari", 2019)
print(s1.firstname, s1.secondname, s1.graduationyear)'''




from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}