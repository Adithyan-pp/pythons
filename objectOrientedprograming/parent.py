class Shipping:

    def calculate_shipping_cost(self,weight):

        print(weight*5)

class Express_shipping(Shipping):

    def calculate_shipping_cost(self,weight):

        print(weight*20)

class Standingshipping(Shipping):

    def calculate_shipping_cost(self,weight):

        print(weight*10)

shipping_exp=Express_shipping()

shipping_exp.calculate_shipping_cost(10)

shipping_stnd=Standingshipping()

shipping_stnd.calculate_shipping_cost(30)

shipping=Shipping()

shipping.calculate_shipping_cost(20)
