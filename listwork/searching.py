# lst=[10,11,12,14,15,16,17]
# element=11

# flag=0
# for num in lst:
#     if element==num:
#         flag=1
#         break
# print("element found" if flag!=0 else "not found")
#
# ##########################################################
#
# flag=0
# for i in range(0,len(lst)):
#     if element==lst[i]:
#         flag=1
#         break
# print("element found" if flag!=0 else "not found")

###########################################################
# lst=[10,11,12,14,15,16,17,12,12,12,12,12,100]
# lst.insert(2,100)
# print(lst)
# lst.append(100)
# print(lst)
#
# lst.pop()
# print(lst)
#
# lst.sort(reverse=True)
# print(lst)
#
# lst.remove(12)
# print(lst)

# oddlist=[]
#
# for num in lst:
#     if num%2!=0:
#         oddlist.append(num)
# print(oddlist)
# oddlist.sort(reverse=True)
# print(oddlist)

# evenlist=[]
#
# for num in lst:
#     if num%2==0:
#         evenlist.append(num)
# print(evenlist)

#############################################################

# lst=[10,11,12,14,15,16,17,12,12,12,12,12,100]
# n=17
# for num in lst:
#     if n==num:
#         print("found")
#         break
#     else:
#         print("not found")
#         break

##############################################################

lst1=[10,11,12,13,14]
lst2=[11,14,15,16,17]

dup_lst=list()

for num in lst1:
    if num in lst2:
        dup_lst.append(num)
print(dup_lst)
