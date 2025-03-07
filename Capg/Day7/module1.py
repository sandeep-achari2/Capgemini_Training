


# Customer Details Class
class Customer_details:
    def __init__(self, cust_id, name, phone, email, address, city, pincode):  # Fixed '__init__'
        self.cust_id = cust_id
        self.name = name  # Added 'self.name'
        self.phone = phone
        self.email = email
        self.address = address
        self.city = city
        self.pincode = pincode

    def get_details(self):
        print(f"Name is {self.name} and address is {self.address}")