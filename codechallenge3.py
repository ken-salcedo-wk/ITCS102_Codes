#CODE CHALLENGE 3

#INPUTS
name = input("Input SENDER NAME ----->  ")
item = input("Input TYPE OF ITEM you want to Buy ----->  ")
isFragile = bool(input("Is the item Fragile? yes/no? ----->  "))
weight = float(input("Input Weight in kg ----->  "))
distance = float(input("Input Distance in km ----->  "))
is_express = bool(input("Is the shipping EXPRESS? yes/no? ----->   "))
is_international = bool(input("Is the shipping INTERNATIONAL yes/no? ----->  "))
base_cost = (weight * 2.50) + (distance * 0.15)


#FORMULA
if weight <= 2 and distance <= 100 and not is_express and not is_international:
	total = 0.00
	print("Shipping rate: Free shipping")
elif is_express and is_international:
	total = (base_cost * 1.40) + 50
	print("Shipping rate: International Express")
elif is_express or (is_international and weight > 20):
	total = (base_cost * 1.20) + 25
	print("Shipping rate: Express or Heavy international")
elif weight > 30 or distance > 1000: 
	total = base_cost + 30
	print("Shipping rate: Oversized")
else:
	total = base_cost
	print("Shipping rate: Standard")


#OUTPUTS
print("-------> Summary of the Transaction <--------")    
print("SENDER: ", name)
print("Type of Item: ", item)
print("Is it Fragile?: ", isFragile)
print("Weight of the Item: ", weight)
print("Distance of Travel: ", distance)
print("Expected Cost: ", total)
