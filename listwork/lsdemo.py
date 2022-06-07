expences=[12000,34000,45000,56000,12000,12000]


for i in range(0,5):
    print(expences[i])

for amount in expences:
    print(amount)


employee_names=["rahul","sabir","surej","ratheesh"]

for i in range(0,len(employee_names)):
    print(employee_names[i])


numbers=[12,13,14,15,16,17,18]

for num in numbers:
    if num%2==0:
        print(num)

#################################

for num in numbers:
    if num>15:
        print(num+1)
    elif num<15:
        print(num-1)
    elif num==15:
        print(num)
######################################

count=0
for num in numbers:
    if num>=14 and num<=18:
        count+=1
print(count)

####################################
count=0
for num in numbers:
    if num in range(14,19):
        count+=1
print(count)

####################################

numbers=[-1,2,0,3,4,5,-2,0,3,4,-5,0,7,0]

p_count=0
z_count=0
n_count=0

for n in numbers:
    if n>0:
        p_count+=1
    elif n<0:
        n_count+=1
    elif n==0:
        z_count+=1
print(f"+ve count {p_count}, -ve count {n_count}, zero count {z_count}")