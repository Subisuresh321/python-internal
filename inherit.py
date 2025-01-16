class Person:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class Account(Person):
    def __init__(self, name, code, pay):
        super().__init__(name, code)
        self.pay = pay

class Admin(Person): 
    def __init__(self, name, code, exp):
        super().__init__(name, code)
        self.exp = exp

class Employee(Account, Admin):
    def __init__(self, name, code, pay, exp):
        super().__init__(name, code, pay)
        self.exp = exp
        
    def get_details(self):
        print(f"Name: {self.name}")
        print(f"Code: {self.code}")
        print(f"Pay: {self.pay}")
        print(f"Experience: {self.exp}")

e1 = Employee("Subi", 12345, 50000, "2yrs")
e1.get_details()
