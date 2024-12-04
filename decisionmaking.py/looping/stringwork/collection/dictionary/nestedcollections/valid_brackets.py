user_input=input("enter bracke")



{
    "{":"}",
    "(":")",
    "[":"]",
    "<":">"

}
symbol_stack=[]
top=-1

is_valid=True
for symbol in user_input:
    if symbol in symbol_dictiory:
        top=top+1
        symbol_stack.append(symbol)
    elif top==-1:

     is_valid==False

    elif symbol == symbol_dictiory.get(symbol_stack[top]):
     top=top-1   
     symbol_stack.pop() 

    else:
        is_valid=False

if len(symbol_stack)==0 and  is_valid==True:
   print("valid")
else:
   print("invalid")


#list_dictionary


