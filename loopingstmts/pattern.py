

for row in range(1,5):
    for col in range(1,5):
        print(col,end="")
    print()


    #new pattern

for row in range(1,5):
    for col in range(1,5):
        print(row,end="")
    print()


    #new pattern

for row in range(1,5):
    for col in range(1,row+1):
        print(col,end="\t")
    print()
print("\n")
    #new pattern

for r in range(1,5):
    for c in range(5,r,-1):
        print("#",end="\t")
    print()
