class Bank:
    def __init__(self,name,type,accnum):
        self.name=name
        self.type=type
        self.accnum=accnum
        self.bal=0
    def get_details(self):
        print(f"Account holder {self.name}")
        print(f"Account type {self.type}")
        print(f"Account number {self.accnum}")
        print(f"Balance {self.bal}")
        
    def getbal(self):
        print(f"Balance of {self.name} is {self.bal}")
    
    def deposit(self,amount):
        if(amount<0):
            return "Enter a valid Amount "
        else:
            self.bal+=amount
            print(f"Deposited {amount}")
            self.getbal()
    
    def withdraw(self,amount):
        if(amount>self.bal):
            return "Insufficent Bal "
        else:
            self.bal-=amount
            print(f"Widrawn {amount}")
            self.getbal()
            
basil=Bank("basil","savings",1234)

subi=Bank("subi","minimum balance",5678)

basil.deposit(2900)
basil.withdraw(1200)

subi.deposit(5000)

basil.getbal()
subi.getbal()  

basil.get_details()
subi.get_details()