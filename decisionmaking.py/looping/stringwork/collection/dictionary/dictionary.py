# create a dictionary product with key id,title,price,brand

product={"id":321,"title":"biscut","price":20,"brand":"oreo"}

print(product["brand"])

product["price"]=30

print(product)

product["exp_date"]="17-5-2024"

print(product)
#add offer as 10 if offer exist else add offer as 20

if "offer" in product:

    product["offer"]=10

else:

    product["offer"]=20

print(product)
