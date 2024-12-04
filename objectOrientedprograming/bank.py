class Bank:

    accno:int

    balance:float

    ac_type:str

    customer_name:str

    def __init__(self,accno,balance,ac_type,customer_name):

        self.accno=accno

        self.balance=balance

        self.ac_type=ac_type

        self.customer_name=customer_name

    def deposit(self,amount):

        self.balance+=amount

    def withdraw(self,amount):

        if self.balance<amount:

            print("insufficient money")

        else:

            self.balance-=amount

            print(f"your amount{self.accno} has been debited with amount{amount} avl bal{self.balance}")

    def get_balance(self):

     print("your aval bal",self.balance)

Bank_instance1=Bank(1111,16000,"saving","akhil")

Bank_instance1.withdraw(20000)

Bank_instance1.deposit(20000)

Bank_instance1.get_balance()