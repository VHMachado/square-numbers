import math
from prettytable import PrettyTable

def ask_number():
    return int(input("Insert a square number: "))

def check_square_number(x):
    x = math.sqrt(x)
    return x.is_integer()

def make_numbers_list(x):
    return list(range(1,x+1))

def get_interval(x):
    return int(math.sqrt(x))

x = ask_number()
is_square = check_square_number(x)

if is_square:
    print("The number is a square number")
else:
    print("The number isn't a square number")

interval = get_interval(x)

unformatted_list = make_numbers_list(x)
formatted_list = list()

for i in range(0, len(unformatted_list), interval):
    formatted_list.append(unformatted_list[i:i+interval])

table = PrettyTable()
table.add_rows(formatted_list)
table.hrules = True
print(table)
