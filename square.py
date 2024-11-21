import math

def check_square_number(x):
    x = math.sqrt(x)
    return x.is_integer()

def make_numbers_list(x):
    return list(range(1,x+1))

def get_interval(x):
    return int(math.sqrt(x))

x = 9
is_square = check_square_number(x)

if is_square:
    print("O número inserido é um número quadrado")
else:
    print("O número inserido não é um número quadrado")

interval = get_interval(x)

list = make_numbers_list(x)

for number in list:
    print(number)