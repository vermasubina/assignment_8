#Q.1
class circle:
    def __init__ (self,rad):
        self.radius=rad
    def getArea(self):
        self.area=3.14*self.radius*self.radius
        return self.area
    def getCircumference(self):
        self.cir=2*3.14*self.radius
        return self.cir
rad=int(input("Enter radius of circle "))
c1=circle(rad)
print("Area of circle is:",c1.getArea())
print("Circumference of circle is:", c1.getCircumference())

#Q.2-
class student:
    def __init__(self,name,rno):
        self.name=name
        self.rollno=rno
    def setAge(self,age):
        self.age=age
    def setMarks(self,marks):
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Roll No.:",self.rollno)
        print("Age:",self.age)
        print("Marks:",self.marks)
name=input("Enter name")
rno=int(input("Enter rollno"))
age=int(input("Enter the age of student "))
marks=int(input("Enter the marks of student "))
s=student(name,rno)
s.setAge(age)
s.setMarks(marks)
s.display() 

#Q.3
class Temperature:
    def convertFahrenheit(self,co):
        f=((co*9)/5)+32
        return f
    def convertCelsius(self,f):
        co=(f-32)/1.8
        return co
tmp=Temperature()
temp=int(input("Enter temperature in Celcius "))
temp1=int(input("Enter temperature in Fahrenheit "))
print(temp,"in Fahrenheit is",tmp.convertFahrenheit(temp),"and",temp1,"in Celclius is",tmp.convertCelsius(temp1))


#Q.4
class MovieDetails:
    def add(self,name,year,rating):
        self.artistname=name
        self.yearofrelease=year
        self.rating=rating
    def display(self):
        print("Artist Name: ",self.artistname,"Year of release:",self.yearofrelease,"Rating:",self.rating)
    
a=MovieDetails()
name=input("Enter name of artist ")
year=int(input("Enter year of release "))
rating=int(input("Enter rating "))
a.add(name,year,rating)
a.display()

#Q.5
class Animal:
    def animal_attribute(self):
        print("My attribute is: Lion")
class Tiger(Animal):
    def tiger_attr(self):
        print(" ")
a=Animal()
t=Tiger()
t.animal_attribute() 

#Q.6-Determine the output of following code.
''''The output will be
A B
A B
because a.f() calls function f() which calls g() which returns 'A' and b.f() calls f() which calls self.g() so this means g() of class B will be called.
a.g() and b.g() will call g() of class A and B respectively. Here, method overriding is done.''' 

#Q.7
class shape:
    def __init__(self,len,brd):
        self.length=len
        self.breadth=brd
    def area(self):
        self.area=self.length*self.breadth
        return self.area
class rect(shape):
    def __init__(self,len,brd):
        self.length=len
        self.breadth=brd
class square(shape):
    def __init__(self,sq):
        self.length=sq
        self.breadth=sq
r=rect(20,2)
s=square(10)
print("Area of rectangle",r.area(),"and area of square:",s.area())
