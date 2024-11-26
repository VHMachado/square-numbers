import math
from prettytable import PrettyTable, SINGLE_BORDER
import pandas as pd
import os
from PIL import Image, ImageDraw, ImageFont

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

        print("Would you like to save the table to a file?")
        save_table = input("(Y)es or (N)o?\n")
        if save_table == "y" or "Y":
            print("Which file format would you like to save the table?\nType in the desired option")
            option = input("(1) text\n(2) csv\n(3) excel\n(4) image\n\nAnswer: ")
            match option:
                case "1":
                    with open("table.txt", "w", encoding="utf-8") as f: f.write(table.get_string())

                case "2": 
                    with open("table.csv", "w", newline="" ,encoding="utf-8") as f: f.write(table.get_csv_string())

                case "3":
                    with open("table.csv", "w", newline="" ,encoding="utf-8") as f: f.write(table.get_csv_string())
                    df = pd.read_csv("table.csv")
                    df.to_excel("table.xlsx", index=False)
                    os.remove("table.csv")

                case "4":
                    # im = Image.new("RGB", (500, 200), "white")
                    # draw = ImageDraw.Draw(im)
                    # font = ImageFont.truetype("FreeMono.ttf", 15)
                    # draw.multiline_text((10, 10), table.get_string(), font=font, fill="black", align="left")

                    # im.show()
                    # im.save("table.png")
                    pass

            print("The file was saved succesfully. Check the program's folder to find it")

        elif save_table == "n" or "N":
            pass
        else:
            print("Invalid response")
            # Repeat if
    else:
        print("The number isn't a square number")
        n1, n2 = calculate_closest_numbers(x_root)
        print(f"The closest square numbers to the one you typed are {n1} and {n2}")

    
