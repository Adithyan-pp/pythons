class mobiles:

    name:str

    price:int

    brand:str

    def _init_(self,name,price,brand):

       self.name=name

       self.price=price

       self.brand=brand

    def display(self):

        print(self.name,self.price,self.brand)

mobile_instance=Mobiles("google pixel 9pro",79000,"pixel")

