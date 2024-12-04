#def student_info(45,43,44,operation="avg")

#def student_info(45,43,44,operation="total")

def student_info(*args,**kwargs):

    if kwargs.get("operation")=="avg":

        return sum(args)

    if kwargs.get("operation")=="total":

        return sum(args)/len(args)

print(student_info(45,43,44,operation="total"))

# def sort_number(1,2,6,4,15,11,reverse="True") desc

# def sort_number(1,2,3,6,4,11,15,reverse="True") 

def sort_number(*args,**kwargs):

    if kwargs.get("reverse")=="True":

        return sorted(args,reverse=True)

    if kwargs.get("reverse")=="false":

        return sorted(args)

print(sort_number(1,2,3,6,4,15,11,reverse="True"))


    