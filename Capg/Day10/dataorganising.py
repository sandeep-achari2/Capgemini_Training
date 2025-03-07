
import csv

class Student:
    def __init__(self,data_input,filename):
        self.data_input=data_input
        self.filename = filename
    
    def write(self):
        try:
            with open(self.filename, mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=self.data_input[0].keys())
                writer.writeheader()
                writer.writerows(self.data_input)
        except FileNotFoundError :
            print(f"Filenot found {self.filename} doesnot exists")

    def read(self):
        try:
            with open(self.filename, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(row)
        except FileNotFoundError:
            print(f"Filenot found {self.filename} doesnot exist")

# Usage
data_input=[
    {"name": "sandeep", "age": 21},
    {"name": "harish", "age": 22}
]

csv_handler = Student(data_input,"data.csv")
csv_handler.write()
csv_handler.read()
