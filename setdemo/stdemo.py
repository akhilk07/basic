

# lst=[10,11,12,13,14,15]
#
# st=set(lst)
# print(st)

st1={1,2,3,4,5}
st2={10,11,12,2,3}
# st1.add(10)
union_set=st1.union(st2)
print(union_set)

intersection_set=st1.intersection(st2)
print(intersection_set)

# diff_set=st1.difference(st2)
# print(diff_set)

students=["ram","ravi","hari","tom","nikhil","jain","john"]
passed_students=["ravi","hari","tom"]

fail_set=set(students).difference(passed_students)
print(fail_set)