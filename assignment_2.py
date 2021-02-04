#!/usr/bin/env python3
# CS300 Project 2: Options Program
# @version 2021/01/24
# @author Chase Renick
"""
The master program prompts users if they want to select from a-e options
varying from calculating a date to calculating the volume of a cylinder.
Master program is designed to handle users messing with system.
"""
import re
from datetime import date
import math
import random
import string


def start_prompt():
    """
    INPUT: None
    OUTPUT: Introduces purposes of program
    """
    return """Welcome to the Python Game Selection Tool. \nProgram Options:\n"""


def end_prompt():
    """
    INPUT: None
    OUTPUT: Prompt when user when they are finished using the program
    """
    return """Finished already? Ok well thanks for playing ;)"""


def error_prompt():
    """
    INPUT: None
    OUTPUT: Generic error prompt when user types in an invalid entry
    """
    return """That is not a valid entry. Try again."""


def contains_special(response):
    """
    :param response: A string of user input
    :return: A boolean value if user entry contains special characters or not
    """
    return bool(re.search(r'[@_!#$%^&*(.)<>?/\|}{~:]', response))


def contains_numbers(response):
    """
    INPUT: A string of user input
    OUTPUT: A boolean value if it is has numbers or not
    """
    return bool(re.search(r'\d', response))


def contains_letters(response):
    """
    A user inputs a value which is then checked against the following regex
    :param response: User input
    :return: A boolean value if a user entry contains letters or not
    """
    return bool(re.search(r'[A-Za-z]', response))


def not_contain_a_g(response):
    """
    Since initial options for users must be from a-f, g-z are not available. Regex checks user input
    :param response: User Input
    :return: A boolean value if a user's entry has
    """
    return bool(re.search(r'[G-Zg-z]', response))


def check_answer(response):
    """
    Checks user response to what game they want to play
    response: A string
    :return: A boolean if it follows the rules
    """
    if contains_numbers(response) or \
            contains_special(response) or \
            not_contain_a_g(response) or \
            len(response) != 1:
        return False
    else:
        return True


def date_calculate():
    """
    Calculates the number of days between today and July 4th 2025
    :return: Delta of days between today's date - future date of July 4th 2025
    """
    day_delta = date.today() - date(2025, 7, 4)
    day_delta = int(day_delta.days)
    if day_delta < 0:
        return "There are {0} until July 4th 2025.".format(str(abs(day_delta)))


def cylinder_volume(radius, height):
    """
    Calculates the volume of a cylinder based on radius and height
    :param radius: The radius of the cylinder
    :param height: The height of the cylinder
    :return: The volume of the cylinder pi*r^2
    """
    return float((math.pi) * (radius ** 2) * height)


def cylinder_prompt():
    """
    Prompts user to specify height & radius of cylinder,
    checks if they typed in numbers, and shows results
    :return: Boolean if the cylinder calculation can execute
    otherwise returns an error prompt
    """
    height = input_function("What height is this cylinder (in inches)? ").strip()
    radius = input_function("What is the radius of the cylinder (in inches)? ").strip()
    if check_melange(height) or \
            check_melange(radius):
        return error_prompt()
    else:
        height = float(height)
        radius = float(radius)
        return "Cylinder Volume:" +str(round(cylinder_volume(radius, height)))+" in^3 (rounded)"


def law_of_cosine(var_a=None, var_b=None, cos_deg=None):
    """
    Calculates the law of cosine and rounds to two decimal places
    :param a: Side a of triangle
    :param b: Side b of triangle
    :param cos_deg: Cosine degree
    :return: Rounded float of Law of Cosine equation:
    c^2 = a^2+b^2+2abcos(C)
    """
    return str(round(math.sqrt(float((var_a ** 2) +
                                     (var_b ** 2) -
                                     (2 * var_a * var_b) *
                                     math.cos(cos_deg))), 2))


def check_melange(response):
    """
    Checks multiple hack or incorrect attempts
    :param response: User input in response to a question
    :return: A boolean if they pass the meta checks
    """
    if contains_letters(response) or \
            contains_special(response) or \
            response is None or \
            response == '':
        return True
    else:
        return False


def cosine_prompt():
    """
    INPUT: None
    :return: A boolean, but also prints out the cosine value
    if user types in numbers to prompts
    """
    var_a = input_function("What is the length of side a? ")
    var_b = input_function("What is the length of side b? ")
    cos_deg = input_function("What is the degree opposite side c? ")

    if check_melange(var_a) or \
            check_melange(var_b) or \
            check_melange(cos_deg):
        return error_prompt()
    else:
        var_a = float(var_a)
        var_b = float(var_b)
        cos_deg = float(cos_deg)
        print("Law of Cosine formula: c = sqrt(a^2 + b^2 - 2ab(cos(C))")
        return "Length of c = " + str(law_of_cosine(var_a, var_b, cos_deg))


def check_password(response):
    """
    A check that the user actually types in a number
    as opposed to another character
    :param response: The user response
    :return:
    """
    if check_melange(response):
        return False
    else:
        return True


def generate_password():
    """
    Generates a randomized password based on
    a user specified length
    :return: A joined string based on the
    randomly selected numbers and characters
    """
    pass_len = input_function("What length do you want dat password? ")
    if check_password(pass_len):
        password = ['Password: ']
        pass_len = int(pass_len)
        for i in range(0, pass_len):
            selection = random.randint(1, 4)
            if selection == 1:
                password.append(random.choice(string.ascii_letters.upper()))
            elif selection == 2:
                password.append(random.choice(str(random.randint(0, 9))))
            elif selection == 3:
                char_list = "[@_!#$%^&*()<>?/\|},{~:]"
                special_num = random.randint(0, 23)
                password.append(char_list[special_num])
            else:
                password.append(random.choice(string.ascii_letters.lower()))

        return ''.join(password)
    return error_prompt()


def game_selection(response):
    """
    :param response: User's selection for
    the program they wish to execute
    :return: A boolean, but also prints out
    the results of one of the selected programes
    """
    if response == 'a':
        print(generate_password())
        return True
    elif response == 'b':
        print(percentage_prompt())
        return True
    elif response == 'c':
        print(date_calculate())
        return True
    elif response == 'd':
        print(cosine_prompt())
        return True
    elif response == 'e':
        print(cylinder_prompt())
        return True
    elif response == 'f':
        return False
    else:
        print(error_prompt())
        return False


def input_function(question):
    """
    Streamlining the user input process
    by lowering all and removing white spaces
    :param question: A question to ask the user
    :return: The character(s) user types
    in response to the posed question
    """
    return input(question).strip().lower()


def all_options():
    """
    Shows user various options for a program
    and then prompts them with what is there selection
    :return: The characters the user types into the input
    """
    print("a. Generate a Secure Password")
    print("b. Calculate and Format a Percentage")
    print("c. How many days from today until July 4, 2025")
    print("d. Use the Law of Cosines to calculate "
          "the leg of a triangle.")
    print("e. Calculate the volume of a Right Circular Cylinder.")
    print("f. Exit")
    print("\nWhat would you like to do?\n")
    return input_function("-> ")


def percentage_calc(numerator, denominator, decimal_places):
    """
    Function
    :param numerator: A digit for the numerator
    :param denominator: A digit for the denominator
    :param decimal_places: The number of decimals user wants
    :return: A formatted version of the num / dem
    to a certain number of decimal places
    """
    specified_dec = "{:." + str(decimal_places) + "f}"
    percent = 100 * (numerator / denominator)
    return str(specified_dec.format(percent))


def percentage_prompt():
    """
    Function checks whether numerator and denominator
    is actually a number
    :return: A boolean, but prints out the num/dem
    to a certain number of digits if user types specifies numbers
    """

    numerator = input_function("What is the numerator? ")
    denominator = input_function("What is the denominator? ")
    decimal_places = input_function("How many decimal places do you want? ")

    if check_melange(numerator) or \
            check_melange(denominator) or \
            check_melange(decimal_places):
        return error_prompt()
    else:
        numerator = float(numerator)
        denominator = float(denominator)
        decimal_places = int(decimal_places)
        return "Percentage: " + \
               percentage_calc(numerator, denominator, decimal_places) + \
               str("%")


# The main block that executes the program
if __name__ == '__main__':
    print(start_prompt())
    while True:
        SELECTION = all_options()
        if check_answer(SELECTION):
            if not game_selection(SELECTION):
                break
            else:
                print("\nProgram Options:\n")
        elif SELECTION in ('exit', 'Exit', 'f'):
            break
        else:
            print("Oops! That is not a valid entry. "
                  "Please select one of options (a,b,c,d,e,f)"
                  " without a '.' or type EXIT to stop.\n")
    print(end_prompt())