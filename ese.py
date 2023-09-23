import string
import random
def greet(name):
	print(f"Hello, I am {name}")

password = string.ascii_letters + string.digits + string.punctuation
password_gen = ''.join(random.choice(password) for i in range (10))