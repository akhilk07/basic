lst=[
    [10,11],
    [13,45],
    [50,15],
    [60,16],
    [70,60]
]
# for sub_list in lst:
#     for num in sub_list:
#         if num>16:
#             print(num)
# print(lst)
#
# flattern_list=[]
# for sub_list in lst:
#     for num in sub_list:
#         flattern_list.append(num)
# print(max(flattern_list))


fltn_list=[num for slist in lst for num in slist]
print(fltn_list)

num_gt_sixt=[num for num in fltn_list if num>16]
print(num_gt_sixt)

odd_num=[num for num in fltn_list if num%2!=0]
print(odd_num)

even_sum=sum([num for num in fltn_list if num%2==0])
print(even_sum)