arr=[10,20,30,40,50,2,4]

even_square={num:num**2 for num in arr if num%2==0}
odd_cubes={num:num**3 for num in arr if num%2!=0}

print(even_square)

print(odd_cubes)