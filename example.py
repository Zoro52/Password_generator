import ese

x = input("Enter name:")
ese.greet("ese")
generate_password = input("Do you wish we generate a password for you? (yes/no) ")
if generate_password == "yes":
	print(ese.password_gen)
else:
	my_password = input("Enter your password:")
	if my_password >= "5":
		print("Password too weak")
	else:
		print("Password strong")
	print(f"your password: {my_password}")