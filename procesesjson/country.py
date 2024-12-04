from json import load

f=open("C:\\Users\\adith\\OneDrive\\Desktop\\Pythonworks\\data_set\\countries.json",encoding="utf-8")

data=load(f)

#print number cuntries

#print(len(data))

#all_country_name=[country.get("name")for country in data]

#print(all_country_name)

all_region=[country.get("region")for country in data]

#print(set(all_region))

region_count={region:all_region.count(region)for region in all_region}

#print(region_count)

max_region_count=max(region_count,key=lambda k:region_count.get(k))

#print(max_region_count,region_count.get(max_region_count))

#capital of a specific country
 
country_capital=[country.get("capital")for country in data if country.get("name")=="India"]

#print(country_capital)

# most border in country

country_border_count={country.get("name"):len(country.get("border",[]))for country in data}

#print(country_border_count)

max_border_country=max(data,key=lambda country:len(country.get("borders",[]))).get("name")

#print(max_border_country)


# most populated country

most_populated_country=max(data,key=lambda country:country.get("population",0)).get("name")

#print(most_populated_country)

#

country_borders=[country.get("borders")for country in data if country.get("name")=="India"][0]

#print(country_borders)


alpha_three_codes=[country.get("borders")for country in data if country.get("name")=="Afghanistan"][0]

for code in alpha_three_codes:

    for country in data:

        if country.get("alpha3Code")==code:

            print(country.get("name"))