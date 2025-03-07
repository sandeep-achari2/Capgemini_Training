from datetime import date
from module1 import Customer_details
from module2 import Order_details
from module3 import Order_items
from module4 import Transaction


# Creating customer
customer1 = Customer_details(1, "Sandeep", 9346, "san@gmail.com", "Medchal", "Hyderabad", 501401)
customer2= Customer_details(2, "harish", 9703, "har@gmail.com", "kurnool", "kurnool", 518003)
# Creating order
order1 = Order_details(11, 1, "success", date.today(), 10)
order2 = Order_details(12, 2, "success", date.today(), 11)
# Creating order item
orderitem1 = Order_items(11, 45, 90, 200, 20)
orderitem2 = Order_items(12, 10, 80, 250, 30)
order1.add_items(orderitem1)  # Adding item to the order
order2.add_items(orderitem2)

# Creating transaction
transaction1 = Transaction(20, customer1, order1)
transaction2=Transaction(30,customer2,order2)

# Printing transaction details
details1=transaction1.get_transaction_details()
details2=transaction2.get_transaction_details()

for key,value in details1.items():
    print(f'{key} : {value}')
    
for key,value in details2.items():
    print(f'{key} : {value}')


