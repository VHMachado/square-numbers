import math
from prettytable import PrettyTable, SINGLE_BORDER

def ask_number():
    return int(input("Insert a square number: "))

def get_x_root(x):
    return math.sqrt(x)

def check_square_number(x_root):
    return x_root.is_integer()

def make_numbers_list(x):
    return list(range(1,x+1))

def get_interval(x):
    return int(math.sqrt(x))

def format_list(unformatted_list, interval):
    formatted_list = list()
    for i in range(0, len(unformatted_list), interval):
        formatted_list.append(unformatted_list[i:i+interval])
    return formatted_list

def draw_table(formatted_list):
    table = PrettyTable()
    table.add_rows(formatted_list)
    table.hrules = True
    table.set_style(SINGLE_BORDER)
    table.header=False
    print(table)
    return table

def calculate_closest_numbers(x_root):
    return pow(int(x_root), 2), pow(int(x_root + 1), 2)

while True:
    x = ask_number()
    x_root = get_x_root(x)
    is_square = check_square_number(x_root)

    if is_square:
        print("The number is a square number")

        interval = get_interval(x)
        unformatted_list = make_numbers_list(x)
        formatted_list = format_list(unformatted_list, interval)

        table = draw_table(formatted_list)

        print("Save to text?")
        save_to_text = input("(Y)es or (N)o?\n")
        if save_to_text == "y" or "Y":
            text = table.get_string()
            with open("text.txt", "w", encoding="utf-8") as f: f.write(text)
        elif save_to_text == "n" or "N":
            pass
        else:
            print("Invalid response")
            # Repeat if
    else:
        print("The number isn't a square number")
        n1, n2 = calculate_closest_numbers(x_root)
        print(f"The closest square numbers to the one you typed are {n1} and {n2}")

    
