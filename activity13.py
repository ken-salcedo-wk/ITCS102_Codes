#write a python program that accepts an integer number as age
#and determines the age group label base of that age input

name = input("Input NAME ----->  ")
age = int(input("Input AGE ------  "))

print("hi," , name, "That age is considered as ")
if age >= 1 and age <= 5:
	print("infant")
elif age >= 6 and age <= 12:
	print("kid")
elif age >= 13 and age <= 19:
	print("teenager")
elif age >= 20 and age <= 29:
	print("early adult hood")
elif age >= 30 and age <= 48:
	print("adult")
elif age >= 49 and age <= 59:
	print("advance adult")
elif age >= 60 and age <= 150:
	print("senior")
else:
	print("inavlid")
