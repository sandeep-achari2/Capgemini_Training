
# # #tuples 
# # ()
# # t=(1,2,3,4)
# # print(t)

# # t=(0,'sandeep',1.2,3)
# # print(t)

# # t=0,'sandeep',1.2,3
# # print(t)

# # t=('abc',('def','ghi'))
# # print(t)

# # t=tuple('spam')
# # print(t)

# # for i in t:
# #     for j in t:
# #         print(i)
        

# # print(t[i][j])

# # # t[i]
# # # t[i][j]
# # # t[i:j]


# #sets in python
# # s1={1,2,3,4,5,10}
# # s2={4,5,6,7,8,3,1,2,3}
# # print(s1)
# # print(s2)

# # #union
# # print("Union",s1|s2)
# # print("Union",s1.union(s2))
# # print("Intersection",s1&s2)
# # print("Intersection",s1.intersection(s2))
# # print("Difference",s1-s2)
# # print("difference",s1.difference(s2))

# # #list to tuple
# # list=[1,2,3,4,5,6,7,8,9,10]
# # t=tuple(list)
# # print(t)


# #oops conecepts in python

# class employee: #class definition
#     def __init__(self,name,age,place,salary,food_allowance,bonus,deduction):   #constructor#self is a keyword
#         self.name=name  #instance variable
#         self.age=age
#         self.place=place
#         self.salary=salary
#         self.food_allowance=food_allowance
#         self.bonus=bonus
#         self.deduction=deduction
        
#     def get_salary(self):
#         return self.salary
    
#     def set_salary(self,salary):
#         if (salary)>=0:
#             self.salary=salary
#         else:
#             print("Invalid salary")
            
#     def get_bonus_salary(self):
#         return self.bonus
    
#     def set_bonus_salary(self,bonus):
#         if bonus>=0:
#             self.bonus=bonus
#         else:
#             print("Invalid bonus")
    
#     def get_deduction_salary(self):
#         return self.deduction
    
#     def set_deduction_salary(self,deduction):
#         if deduction>=0:
#             self.deduction=deduction
#         else:
#             print("Invalid deduction")
    
#     def get_food_allowances(self):
#         return self.food_allowances
    
#     def set_food_allowances(self,food_allowances):
#         if food_allowances>=0:
#             self.food_allowance=food_allowances
#         else:
#             print("Invalid deduction")
    
#     def display(self): #instance method
#         print("Name:",self.name) 
#         print("Age:",self.age)
#         print("Place:",self.place)
#         print("Salary:",self.salary)
#         print("Bonus Salary:",self.salary+self.bonus)
#         print("Deduction salary:",self.salary-self.deduction)
#         print("Remaining salary after Food allowances:",self.salary-self.food_allowance)
        
        
# def main():#main function
#     name=input("Enter a name:")
#     age=int(input("Enter Your age:"))
#     place=input("Enter place:")
#     salary=int(input("Enter Salary:"))
#     bonus=int(input("Enter Bonus amount:"))
#     deduction=int(input("enter deduction amount:"))
#     food_allowance=int(input("Enter Food allowances:"))
    
#     e1=employee(name,age,place,salary,food_allowance,bonus,deduction)
#     e1.display()
#     e1.set_salary(salary)
#     e1.set_bonus_salary(bonus)
#     e1.set_deduction_salary(deduction)
#     e1.set_food_allowances(food_allowance)
            
# main()

# #example for an inheritancee

# # class Parent:
# #     def display_parent_class(self):
# #         print("This is a Parent class")
        
# # class Child(Parent):
# #     def display_child_class(self):
# #         print("This is a child class")
        

# # if __name__ == '__main__':
# #     child=Child()
# #     child.display_child_class()
# #     child.display_parent_class()
    

# # class Parent:
# #     def __init__(self):
# #         self.bignose='20cm'
        
# #     def parent_class(self):
# #         print("This is a parent class")
        
# # class Child(Parent):
# #     def __init__(self):
# #         super().__init__()        #for calling child with another variable super keyword is used 
# #         self.smallnose="2cm"
        
# #     def child_class(self):
# #         print("This is a child class")
        
# # child=Child()
# # child.parent_class()
# # child.child_class()
# # print(child.bignose)
# # print(child.smallnose)

# #This is an example how inheritence can can work with parent,subchild,child 

# # class School:
# #     def __init__(self,stud_name,school_name="Vignan"):
# #         self.stud_name=stud_name
# #         self.school_name=school_name
        
# #     def school_class(self):
# #         print(f"Student {self.stud_name} School class{self.school_class} is Generated")
        
# # class Ug_pgm(School):
# #     def __init__(self,name,school_name,clg_name="Raos jr"):
# #         super().__init__(name,clg_name)
# #         self.name=name
# #         self.clg_name=clg_name
    
# #     def ug_program(self):
# #         print("Undergraduation Program is Working")
        

# # class Pg_pgm(Ug_pgm):
# #     def __init__(self,name,school_name,clg_name,inst_name="Cmr"):
# #         super().__init__(name,inst_name)
# #         self.name=name
# #         self.inst_name=inst_name
    
# #     def pg_program(self):
# #         print("Post graduation is working")
    

# # name=input("enter name:")

# # program=Pg_pgm(name,"Vignan","Raos jr")
# # program.school_class()
# # program.ug_program()
# # program.pg_program()

