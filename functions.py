def greet_user():
    print("Hello")

greet_user()

def greet_user(user_name):
    print(f"Hello, {user_name}")
greet_user('Emily')

def describe_zodia(zodia, bunch):
    print(f"{zodia.title()} is {bunch} bunch")
    print(f"Zodiz {zodia.title()} is symbolized as {bunch} bunch")
    print(f"{zodia.title()} is one of the zodiz signs")

describe_zodia('cancer', 'water')
describe_zodia('libra', 'air')