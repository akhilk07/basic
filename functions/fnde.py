def add_numbers(n1,n2):
    return n1+n2
print(add_numbers(10,20))

def sum_numbers(n1,n2):
    return n1-n2
print(sum_numbers(10,5))

def smart_sub(n1,n2):
    return n1-n2 if n1>n2 else n2-n1

def num_chk(num):
    return "even" if num%2==0 else "odd"

print(smart_sub(5,10))
print(num_chk(12))



def is_starts_with(name):
    return name.startswith("a")
name="technolab"
print(name.endswith("lab"))


def variable_gmail(email):
    print(validate_gmail("abc@gmail.com"))

def validate_gmail(email):
    return email.endswith("@gmail.com")
print(variable_gmail("akhilk2091@gmail.com"))


def factorial(num):
    fact=1
    for i in range(1,(num+1)):
        fact=fact*i
        return fact
print(factorial(3))


cube=lambda n:n**3

sub=lambda n1,n2:n1-n2

div=lambda ni,n2:n1/n2

mul=lambda n1,n2:n1*n2



sq=lambda n:n**2

cu=lambda n:n**3

add=lambda n:n1+n2

mtwo=lambda n1,n2:n1 if n1>n2 else n2

rng=lambda low,upp:sum(range(low,upp))
