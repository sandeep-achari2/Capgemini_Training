
# from abc import ABC,abstractmethod

# class Mail():
#     @abstractmethod
#     def send(self):
#         pass
    
# class Email(Mail):
#     def __init__(self,name,email):
#         self.name=name
#         self.email=email

#     def send(self):
#         print(f'{self.name} has received a mail {self.email}')
        
# class Sms(Mail):
#     def __init__(self,name,sms):
#         self.name=name
#         self.sms=sms
        
#     def send(self):
#         print(f"{self.name} has received a sms {self.sms}")


# class Whatsapp(Email):
#     def __init__(self,name,whatsapp):
#         self.name=name
#         self.whatsapp=whatsapp
    
#     def send(self):
#         print(f"{self.name} has received a whatsapp {self.whatsapp}")
        
        
# name=input("enter name: ")
# email=input("enter emails: ")
# sms=input("enter sms:")
# whatsapp=input("enter whatsaap message: ")

# emails=Email(name,email)
# smss=Sms(name,sms)
# whatsappmsg=Whatsapp(name,whatsapp)

# emails.send()
# smss.send()
# whatsappmsg.send()



# from abc import ABC, abstractmethod
# from typing import List

# # Step 1: Define Employee interface using Abstract Base Class (ABC)
# class Employee(ABC):
#     @abstractmethod
#     def work(self) -> str:
#         pass

#     @abstractmethod
#     def get_salary(self) -> float:
#         pass
    
#     @abstractmethod
#     def increase_salary(self, percentage: float) -> None:
#         pass

# # Step 2: Create concrete classes for different types of employees
# class Manager(Employee):
#     def __init__(self, name: str, salary: float):
#         self.name = name
#         self.salary = salary

#     def work(self) -> str:
#         return f"{self.name} is managing the team."

#     def get_salary(self) -> float:
#         return self.salary
    
#     def increase_salary(self, percentage: float) -> None:
#         self.salary += self.salary * (percentage / 100)

# class Developer(Employee):
#     def __init__(self, name: str, salary: float):
#         self.name = name
#         self.salary = salary

#     def work(self) -> str:
#         return f"{self.name} is writing code."

#     def get_salary(self) -> float:
#         return self.salary
    
#     def increase_salary(self, percentage: float) -> None:
#         self.salary += self.salary * (percentage / 100)

# class Intern(Employee):
#     def __init__(self, name: str, salary: float):
#         self.name = name
#         self.salary = salary

#     def work(self) -> str:
#         return f"{self.name} is learning and assisting."

#     def get_salary(self) -> float:
#         return self.salary
    
#     def increase_salary(self, percentage: float) -> None:
#         self.salary += self.salary * (percentage / 100)

# class Security(Employee):
#     def __init__(self, name: str, salary: float):
#         self.name = name
#         self.salary = salary

#     def work(self) -> str:
#         return f"{self.name} is securing the assets."

#     def get_salary(self) -> float:
#         return self.salary
    
#     def increase_salary(self, percentage: float) -> None:
#         self.salary += self.salary * (percentage / 100)

# # Step 3: Define Department class that manages Employees
# class Department:
#     def __init__(self, name: str):
#         self.name = name
#         self.employees: List[Employee] = []

#     def hire(self, employee: Employee) -> None:
#         self.employees.append(employee)
#         print(f"{employee.name} has been hired.")

#     def fire(self, employee: Employee) -> None:
#         self.employees.remove(employee)
#         print(f"{employee.name} has been fired.")

#     def get_total_salary(self) -> float:
#         return sum(employee.get_salary() for employee in self.employees)

#     def show_employee_details(self) -> None:
#         print(f"Employees in {self.name} Department:")
#         for employee in self.employees:
#             print(f"- {employee.name}, Salary: {employee.get_salary()}, Role: {employee.work()}")
    
#     def promote(self, employee: Employee, percentage: float) -> None:
#         if employee in self.employees:
#             employee.increase_salary(percentage)
#             print(f"{employee.name} has been promoted with a {percentage}% salary increase.")
#         else:
#             print(f"{employee.name} is not in the department.")

# # Step 4: Create department and add employees
# # Create employees
# manager = Manager("sandeep", 80000)
# developer = Developer("harish", 60000)
# intern = Intern("raghu", 20000)
# securitystaff = Security("deepu", 5000)

# # Create a department and hire employees
# it_department = Department("IT")
# it_department.hire(manager)
# it_department.hire(developer)
# it_department.hire(intern)
# it_department.hire(securitystaff)

# # Show employee details
# it_department.show_employee_details()

# # Total salary 
# total_salary = it_department.get_total_salary()
# print(f"Total salary expense for {it_department.name} department: ${total_salary}")

# # Promotion
# it_department.promote(developer, 10)
# it_department.promote(intern, 15)

# # updated employee details
# it_department.show_employee_details()

# # Updated total salary 
# total_salary = it_department.get_total_salary()
# print(f"Updated total salary expense for {it_department.name} department: ${total_salary}")


# import os

# cad=os.getcwd()
# print(f'current working directory {cad}')

# files==os.listdir(cad)

