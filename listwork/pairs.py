lst=[2,3,4,6,5]
#
# sum=8
#
# for i in range(len(lst)):
#     for j in range((i+1),len(lst)):
#         cur_sum=lst[i]+lst[j]
#         if cur_sum==sum:
#             print(f"pairs {lst[i]},{lst[j]}")
#             break


low=0
upp=len(lst)-1

while(low<upp):
    cur_sum=lst[low]+lst[upp]

    if element==cur_sum:
        print(f"pairs{lst[upp]},{lst[low]}")
        break
    elif cur_sum>element:
        upp-=1
