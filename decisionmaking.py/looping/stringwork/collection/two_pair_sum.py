arr=[2,3,4,5,6,7,8,9]

left=0
right=len(arr)-1

cur_sum=arr[left],arr[right]

while(left<right):

    if cur_sum==sum:
        print(arr)
       
        break

    elif cur_sum>sum:
        right+=1

    elif cur_sum<sum:

        left+=1