car={"name":"swift","color":"grey","make":"2015","brand":"maruthi","fuel":"petrol","price":"9lac"}


print(car["brand"])

print(car["fuel"])
print("transmission_type" in car)

car["transmission_type"]="manual"
print(car)

print("break_type" in car)
car["break_type"]="abs"
print(car)
