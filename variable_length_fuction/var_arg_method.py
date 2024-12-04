def add_numbers(*args):

    return sum(args)


#create a fuction that accepet any number of arguments and return second maximum number


def second_max_number(*args):

    sorted_numbers=sorted(args,reverse=True)

    return sorted_numbers[1]

#print(second_max_number(10,11,12,13))

def display_mobile_data(**kwargs):

   # print(kwargs.get("name"))

    #print(kwargs.get("price"))

    print(kwargs.get("display"))

display_mobile_data(name="redmi",price=22000,display="amoled")


#caculator(10,20,30,operation="+")

#caculator(10,11,12,13,14,operation="*")

def caculator(*args,**kwargs):

    if kwargs.get("operation")=="+":

        return sum(args)

    if kwargs.get("operation")=="*":

        result=1

        for num in args:

            result=result*num

        return result

print(caculator(10,20,30,operation="*"))
