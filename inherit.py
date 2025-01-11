class Person:
    def __init__(self,name,code):
        self.name=name
        self.code=code
class Account(Person):
    def __init__(self,name,code,pay):
        Person.__init__(self,name,code)
        self.pay=pay
class Admin(Person): 
    def __init__(self,name,code,exp):
        Person.__init__(self,name,code)
        self.exp=exp
class Employee(Account,Admin):
    def __init__(self,name,code,pay,exp):
        Account.__init__(self,name,code,pay)
        Admin.__init__(self,name,code,exp)
        
    def get_details(self):
        print(f"Name : {self.name}")
        print(f"Code : {self.code}")
        print(f"pay : {self.pay}")
        print(f"Exp : {self.exp}")

e1=Employee("Subi",12345,50000,"2yrs")
e1.get_details()