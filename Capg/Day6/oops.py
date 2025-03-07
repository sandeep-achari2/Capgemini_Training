
#constructor with overloading
#call another method inside constructor
#static variable and constructor

#polymorphism allows the same method name to behave different based on the object


# class Cat:
#     def sound(self):
#         print("Meow")

# class Dog:
#     def sound(self):
#         print("Bark")
          
# for animal in[Cat(),Dog()]:
#     animal.sound()
    
    
# class Father:
#     def sound(self):
#        print("focus on study")
        
# class Mother:
#     def sound(self):
#         print("focus on goal")
        
# for message in [Father(),Mother()]:
#     message.sound()

# import dis
# class School:
#     school_name="Vignan school"
#     def __init__(self,name):
#         self.name=name
#     def get_name(self):
#         return self.name
# name=School("sandeep")
# dis.dis(name)
# print(name.get_name())
# print(name.school_name)
# School.school_name="abc"
# dis.dis(name.school_name)
# print(name.school_name)

# class Sample1:
#     def student(self,name):
#         return self.name
    
# class Sample2():
#     def student(self,rollname):
#         return self.rollname
    
# name=input("input name:")
# rollname=input("Enter roll no:")
# obj=Sample2()
# for obj in [Sample1(),Sample2()]:
#     obj.student()
    
    
# class Exercise:
#     def __init__(self,name):
#         print(f'first constuctor: Hello {name}')
    
#     def __init__(self,age):
#         print(f'second constructor age is: {age}')
        
# obj=Exercise(25)#create object

# class Exercise:
#     def __init__(self,*args):
#         if len(args)==1:
#             print(f"hello {args}")
#         elif len(args)==2:
#             print(f"Hello {args[0]}, you are {args[1]}")
            
# obj=Exercise(23)

# class Exercise:
#     def __init__(self,student_name,**kwargs):
#         self.student_name=student_name
#         if "name" in kwargs and "age" in kwargs:
#             print(f"hello {kwargs['name']},you are {age} age")
#         elif "name" in kwargs:
#             print(f"Hello {kwargs['name']}")
#         self.xfield=kwargs.get('name')
        
# # Taking real-time input
# name=input("enter name:")
# person_name = input("Enter person's name: ")
# age=int(input("enter age:"))
# # Creating object with keyword arguments
# obj1 = Exercise(name, name=person_name, age=age)

# # Accessing attributes
# obj1.student_name
# obj1.xfield
            
# class Destructorexample:
#     def __init__(self,name):
#         self.name=name
#         print(f"object {self.name} is created.")
        
#     def __del__(self):
#         print(f'object {self.name} is destroyed')
        
        
# obj=Destructorexample("Sandeep")
# del obj            
            
#multiple inheritance example
# #parent class    
# class Parent:
#     def fly(self):
#         print("Bird is flying")

# class Mammal:
#     def walk(self):
#         print("mammal is walking")

# class Bat(Parent,Mammal):
#     pass

# bat=Bat()
# print(bat.fly())
# print(bat.walk())
            

#multilevel inheritance

#heiirachiel inheitance
# #parent class
# class Shape:
#     def area(self):
#         pass

# #child class1
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
        
#     def area(self):
#         return 3.14*self.radius**2
    
# #child class 2
# class Square(Shape):
#     def __init__(self, side):  # Fixed __init__ method
#         self.side = side  # Initializing side

#     def area(self):
#         return self.side ** 2
    
# radius=float(input("enter radius of circle:"))
# side=float(input("Enter side of the square:"))
# obj1=Circle(radius)
# obj2=Square(side)
# print(f"Area of Circle: {obj1.area():.2f}")
# print(f"Area of Square: {obj2.area():.2f}")


from datetime import date
#example
class Customer_details:
    def __init__(self,cust_id,name,phone,email,address,city,pincode):
        self.cust_id=cust_id
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
        self.city=city
        self.pincode=pincode
        
    def get_details(self):
        print(f"Name is {self.name} and address is {self.address}")

class Order_details(Customer_details):
    def __init__(self,order_id,cust_id,order_status,order_date,store_id):
        self.order_id=order_id
        self.cust_id=cust_id
        self.order_status=order_status
        self.order_date=order_date
        self.store_id=store_id
        self.list_items=[]
    
    def add_items(self,item):
        self.list_items.append(item)
        
    def total_item_prices(self):
        return sum(self.item.get_total() for item in self.list_items)
    

class Order_items:
    def __init__(self,order_id,product_id,quantity,price_list,discount):
        self.order_id=order_id
        self.product_id=product_id
        self.quantity=quantity
        self.price_list=price_list
        self.discount=discount
        
    def get_total(self):
        return self.quantity*self.price_list*(1-self.discount/100)
           
        
class Transaction:
    def __init__(self,transaction_id,customer,order):
        self.transaction_id=transaction_id
        self.customer=customer
        self.order=order
        
    def get_transaction_details(self):
        print("Transaction ID:",self.transaction_id)
        print("Customer name:",self.customer)
        print("Order id:",self.order.order_id)
        print(f"Total amount: {self.order.total_item_prices(): .2f}")
        print(f"Order details: {[{'productid': item.product_id, 'Quantity': item.quantity, 'Price': item.get_total()} for item in self.order.list_items]}")

        
        
#creating cust_id,name,phone,email,address,city,pincode
customer1=Customer_details(1,"sandeep",9346,"san@gmail.com","Medchal","hyderabad",501401)

#creating order order_id,cust_id,order_status,order_date,store_id
order=Order_details(11,1,"success",date.today(),10)

#order_id,product_id,quantity,price_list,discount
orderitem1=Order_items(11,45,90,200,20)

#transaction_id,customer,order
transaction1=Transaction(20,customer1,order)

#print
details=transaction1.get_transaction_details()
for key,value in details.list_items():
    print(f"{key} : {value}")
    
        
        
    
    
    
    
    
    
    
        