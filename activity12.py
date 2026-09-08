#import getpass
from getpass import getpass

username = 'user1'
password = 'pogiako123'

u = input("Enter Username ====>  ")
p = getpass("Enter Password ====>  ")
#p = getpass.getpass("Enter Password ====>  ")

if username == u and password == p :
	print("ACCESS GRANTED")
else:
	print("ACCESS DENIED")