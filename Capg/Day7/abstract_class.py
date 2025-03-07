

# from abc import ABC,abstractmethod

# class Father(ABC):
#     @abstractmethod
#     def display(self):
#         pass
    
#     def show(self):
#         print("Concrete Method")
        
# class Son(Father):
#     def display(self):
#         print("Son is implementing abstract method")


# class Daughter(Father):
#     def display(self):
#         print("daughter is implementing abstract class")


# a=Son()
# a.display()
# a.show()
# b=Daughter()
# b.display()

# from abc import ABC,abstractmethod

# class Father(ABC):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#     @abstractmethod
#     def display(self):
#         pass

#     def pan_details(self,pan_no):
#         self.pan_no=pan_no

# class Son(Father):
#     def __init__(self,name,age):
#         super().__init__(name,age)
        
#     def display(self):
#         print(f'Son name {self.name} , at age {self.age}, son pan number {self.pan_no}')
        
# class Daughter(Father):
#     def __init__(self,name,age):
#         super().__init__(name,age)
#     def display(self):
#         print(f'Daughter name is {self.name} , age is {self.age} , daughter pan number is {self.pan_no} ')
        
# son=Son("sandeep",22)
# daughter=Daughter("vasantha",21)
# son.pan_details("opgpsdse2342")
# daughter.pan_details("khmsshdakd13")
# son.display()
# daughter.display()

    
# from abc import ABC,abstractmethod

# class Person(ABC):
    
#     @abstractmethod
#     def display(self):
#         pass
    
#     def calculation(self):
#         pass
    
# class Father(Person):
#     def display(self):
#         print("Display function is working")
    
#     def calculation(self):
#         print("Calculation is Working")
        
# father=Father()
# father.display()
# father.calculation()

#basic Abstract implementation
# from abc import ABC,abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
    
    
# class Dog(Animal):
#     def make_sound(self):
#         print("Bark!")
        
# class Cat(Animal):
#     def make_sound(self):
#         print("Meow")
        
# dog=Dog()
# cat=Cat()
# dog.make_sound()
# cat.make_sound()


#Abstract Class with Constructor

# from abc import ABC,abstractmethod

# class Vechile(ABC):
#     def __init__(self,brand):
#         self.brand=brand

#     @abstractmethod
#     def max_speed(self):
#         pass
    
# class Car(Vechile):
#     def max_speed(self):
#         print(f"{self.brand} Car have speed of 200kmph")

# class Bike(Vechile):
#     def max_speed(self):
#         print(f"{self.brand} Bike have speed of 150kmph")
        

# car=Car("Tesla")
# bike=Bike("Honda")

# car.max_speed()
# bike.max_speed()
    

#Using Abstract Methods in Derived Classes
# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         return self.length * self.breadth

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2

# r = Rectangle(5, 10)
# c = Circle(7)

# print(f"Rectangle Area: {r.area()}")
# print(f"Circle Area: {c.area()}")  

from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def profession(self):
        pass

    def introduce(self):
        print("I am a father.")
        self.profession()

class Engineer(Father):
    def profession(self):
        print("I am an Engineer.")

class Doctor(Father):
    def profession(self):
        print("I am a Doctor.")

e = Engineer()
e.introduce()

d = Doctor()
d.introduce()
