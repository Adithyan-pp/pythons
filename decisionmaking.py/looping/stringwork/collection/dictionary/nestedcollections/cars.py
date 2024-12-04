cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt"]},
]

print(f"total vehicles=>{len(cars)}")

#print available colors of baleno

baleno_colors=[c.get("colors")for c in cars if c.get("name")=="baleno"]

print(baleno_colors)

print(baleno_colors[0])

#print all brands 

brands=[c.get("brand")for c in cars ]

brand_count={b for b in brands}

print(set(brand_count))
#print car names available in amt transmission

amt_cars=[c.get("name") for c in cars if "amt" in c.get("transmissions")]

print(amt_cars)
# cars available in blue color

blue_color=[c.get("name")for c in cars if "blue" in c.get ("colors")]

print(blue_color)

# print all amt_transmission types

all_transmission={ t for c in cars for t in c.get ("transmissions")}

print(all_transmission)
# print the colors of cars 

all_colors={color for c in cars for color in c.get("colors")}

print(all_colors)

color=[colo for c in cars for colo in c.get("colors")]

color_count={co:color.count(co)for co in color}

print(color_count)

#costly cars 

# costly cars
costly_car=max(cars,key=lambda d:d.get("price"))

max_price=costly_car.get("price")

costly_cars=[m.get("name") for m in cars if m.get("price")==max_price]

print(costly_cars)

# car with minimum cost 
mincost_car=min(cars,key=lambda d:d.get("price"))

min_price=mincost_car.get("price")

mincost_cars=[m.get("name") for m in cars if m.get("price")==min_price]

print(mincost_cars)

#sort cars with price 

sorted_car=sorted(cars,key=lambda d:d.get("price"),reverse=True)

sorted_car_name={c.get("name"):[c.get("price"),c.get("brand")] for c in sorted_car}

print(sorted_car_name)