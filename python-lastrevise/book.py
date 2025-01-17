class Publisher:
    def __init__(self,name):
        self.name=name
class Book(Publisher):
    def __init__(self,name,author,title):
        super().__init__(name)
        self.author=author
        self.title=title
    def get_details(self):
        print(f"Name : {self.name}")
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")

class Python(Book):
    def __init__(self, name, author, title,price,pageno):
        super().__init__(name, author, title)
        self.price=price
        self.pageno=pageno
    def get_details(self):
        super().get_details()
        print(f"Page No : {self.pageno}")
        print(f"Price : {self.price}")
        
p1=Python("ABC BOOKS","Subi","Hai Python",1200,250)
p1.get_details()

p2=Book("DC BOOKS","joker","koi")
p2.get_details()        
    