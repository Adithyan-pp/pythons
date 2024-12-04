arr=[10,13,15,20,17,19]

arr.sort()

search_element=int(input("enter the number to  search:"))

is_present=False

low=0

upp=len(arr)



while(low<=upp):

 mid=(low+upp)//2

 if search_element==arr[mid]:

  is_present=True

  break

 elif search_element<arr[mid]:

  upp=mid-1

 elif search_element>arr[mid]:

  low=mid+1

print(is_present)