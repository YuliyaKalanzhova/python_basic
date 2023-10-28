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

describe_zodia(zodia = 'Libra', bunch = 'Air')

def describe_zodia(zodia, bunch, zodia_number = 12):
    print(f"{zodia.title()} is one of the {bunch} bunches in {zodia_number} zodia circle")

describe_zodia('libra', 'air')

def get_full_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

return_full_name = get_full_name("Jon", "Jonson")
print(return_full_name)

def get_full_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("Fill in the form and provide with the full name: ")
    f_name = input("Your name: ")
    if f_name == 'quit':
        break

    l_name = input("Your last name: ")
    if l_name == 'quit':
        break
    
    full_name = get_full_name(f_name, l_name)
    print(f"Hello {full_name}")

def greet_users(names):
    for name in names:
        print(name.title())

user_names = ["Jon", "Jey"]
greet_users(user_names)

paints = ['phone', 'computer', 'horse']
completed = []

while paints:
    current= paints.pop()
    print(current)
    completed.append(current)

for i in completed:
    print(i)

def print_paints(paints, completed):
    while paints:
        current = paints.pop()
        completed.append(current)

def print_completed(completed):
    for image in completed:
        print(image)

paints = ['phone', 'computer', 'horse']
completed = []

print_paints(paints, completed)
print_completed(completed)

paints2 = ['mouse', 'keybord', 'box']
completed2 = []

print_paints(paints2, completed2)
print_completed(completed2)

def make_pizza(size, *adds):
    print(f"This pizza {size} size consists of: ")
    for add in adds:
        print(add)

make_pizza(21, 'cheese')
make_pizza(22, 'cheese', 'tomato')

