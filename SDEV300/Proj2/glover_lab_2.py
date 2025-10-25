"""
_filename: "glover_lab_2.py
_course name: "SDEV300 6382"
_author: "Corey Glover"
_copyright: "None"
_credits: ["Corey Glover", "Craig Poma"]
_license: "GPL"
_version: "1.0.0"
_maintainer: "Corey Glover"
_email: "corey.j.glover@student.umgc.edu"
_description: "This program displays a menu then
        asks user which function to perform or exit."
"""
# import packages needed in program
import string
import sys
from datetime import datetime
import math
import secrets
import numpy

# list of all variables that will build the user password
PW_SET = ({
    'PW_UPPER': string.ascii_uppercase,
    'PW_LOWER': string.ascii_lowercase,
    'PW_NUMBER': string.digits,
    'PW_SPEC_CHAR': string.punctuation
})


# function for the main program
def main():
    """
    main program function
    :return:
    """
    user_menu()


# function to display menu for user choices
def user_menu():
    """
    Displays user menu and allows user to enter their choice.\
    :param: choice
    """
    while True:
        # print menu
        print("***************MENU************")
        print("""
        1: Generate Secure Password
        2: Calculate and Format a Percentage
        3: How many days from today until July 4, 2025?
        4: Use the Law of Cosines to calculate the leg of a triangle.
        5: Calculate the volume of a Right Circular Cylinder
        0: Exit
        """)
        print("*******************************")
        # handle user choice of menu items
        choice = input("Please select an item: ")
        if choice == '1':
            generate_pw()
        elif choice == '2':
            calculate_percent()
        elif choice == '3':
            calculate_days()
        elif choice == '4':
            calculate_triangle()
        elif choice == '5':
            calculate_vol()
        elif choice == '0':
            print("Thank you for using the application.")
            sys.exit()
        else:
            print("That is not a valid selection.")


# set uppercase limit
def upper_limit():
    """
    function to generate limit of upper characters
    :param: pw_upper, pw_upper_limit
    :exception: if user chooses something other than allowable values
    :return: pw_upper_limit
    """
    # while loop that handles if user inputs length and how long
    pw_upper_limit = -1
    while pw_upper_limit < 0:
        try:
            pw_upper_limit = int(input("\t# How many uppercase characters "
                                       "should be included? "))
        except TypeError:
            print("\t### Please try again.")
        else:
            return pw_upper_limit


# create uppercase letters for user pw
def generate_upper(pw_upper_limit):
    """
    function to generate a string of uppercase letters
    :param: user_pw, pw_upper, pw_upper_limit
    :exception: if user chooses something other than allowable values
    :return: user_pw
    """
    # while loop and for loop that create the uppercase string
    while pw_upper_limit > 0:
        user_pw = ''
        try:
            for _ in range(pw_upper_limit):
                user_pw += secrets.choice(PW_SET['PW_UPPER'])
        except ValueError:
            print("\t### Please verify input.")
        else:
            print("upper: ", user_pw)
            return user_pw


# get lowercase limit
def lower_limit():
    """
    function to generate limit of upper characters
    :param: pw_lower, pw_lower_limit
    :exception: if user chooses something other than allowable values
    :return: pw_lower_limit
    """
    pw_lower_limit = -1
    while pw_lower_limit < 0:
        try:
            pw_lower_limit = int(input("\t# How many lowercase characters"
                                       " should be included? "))
        except TypeError:
            print("\t### Please try again.")
        else:
            return pw_lower_limit


# generate lowercase letters for user pw
def generate_lower(pw_lower_limit):
    """
    function to generate a string of uppercase letters
    :param: user_pw, pw_lower, pw_lower_limit
    :exception: if user chooses something other than allowable values
    :return: user_pw
    """
    # while loop and for loop that create the lowercase character string
    while pw_lower_limit > 0:
        user_pw = ''
        try:
            for _ in range(pw_lower_limit):
                user_pw += secrets.choice(PW_SET['PW_LOWER'])
        except ValueError:
            print("\t### Please verify input.")
        else:
            print("lower: ", user_pw)
            return user_pw


# get the limit of numbers
def numbers_limit():
    """
    function to generate limit of number characters
    :param: pw_number, pw_number_limit
    :exception: if user chooses something other than allowable values
    :return: pw_number_limit
    """
    pw_number_limit = -1
    while pw_number_limit < 0:
        try:
            pw_number_limit = int(input("\t# How many numbers"
                                        " should be included? "))
        except TypeError:
            print("\t### Please try again.")
        else:
            return pw_number_limit


# generate numbers for user pw
def generate_numbers(pw_number_limit):
    """
    function to generate a string of uppercase letters
    :param: user_pw, pw_number_limit
    :exception: if user chooses something other than allowable values
    :return: user_pw
    """
    # while loop and for loop that create the number string
    while pw_number_limit > 0:
        user_pw = ''
        try:
            for _ in range(pw_number_limit):
                user_pw += secrets.choice(PW_SET['PW_NUMBER'])
        except ValueError:
            print("\t### Please verify input.")
        else:
            print("numbers: ", user_pw)
            return user_pw


# get limit of spec char
def spec_char_limit():
    """
    function to generate limit of upper characters
    :param: pw_spec_charc, pw_spec_limit
    :exception: if user chooses something other than allowable values
    :return: pw_spec_limit
    """
    pw_spec_limit = -1
    while pw_spec_limit < 0:
        try:
            pw_spec_limit = int(input("\t# How many special characters"
                                      " should be included? "))
        except ValueError:
            print("\t ### Please try again.")
        else:
            return pw_spec_limit


# generate spec char for user pw
def generate_spec_char(pw_spec_limit):
    """
    function to generate a string of spec characters
    :param: user_pw, pw_spec_limit
    :exception: if user chooses something other than allowable values
    :return: user_pw
    """
    # while loop and for loop that create the special character string
    while pw_spec_limit > 0:
        user_pw = ''
        try:
            for _ in range(pw_spec_limit):
                user_pw += secrets.choice(PW_SET['PW_SPEC_CHAR'])
        except ValueError:
            print("\t ###Please verify input.")
        else:
            print("spec: ", user_pw)
            return user_pw


def get_pw_limit():
    """
    function to get the limit of the pw
    :return:
    """
    pw_upper_limit = upper_limit()
    pw_lower_limit = lower_limit()
    pw_number_limit = numbers_limit()
    pw_spec_limit = spec_char_limit()
    pw_limit = pw_upper_limit + pw_lower_limit \
               + pw_spec_limit + pw_number_limit
    return {
            'LIMIT': pw_limit,
            'PW_UPPER': pw_upper_limit,
            'PW_LOWER': pw_lower_limit,
            'PW_SPEC_CHAR': pw_spec_limit,
            'PW_NUMBER': pw_number_limit,
           }


# function to generate the password
def generate_pw():
    """
    function to create a password
    :param: user_pw, pw_length, pw_limit, pw_test,
        char_type, user_pw, pw_list, user_pw_set
    :exception: if password doesn't meet posted parameters
    :return: break, user_pw_set
    """
    user_pw_set = None
    while user_pw_set is None:
        try:
            user_pw = ''
            pw_length = int(input("\tPlease input the length "
                                  "of password to generate: "))
            # if statement that keeps pw length to general strong pw length
            if 12 <= pw_length <= 64:
                pw_limit = get_pw_limit()
                if pw_limit['LIMIT'] < pw_length:
                    print('#' * 80)
                    print(f"\t### Please keep password characters to the set"
                          f" length entered of {pw_length}.")
                    return
                # removes the item total from list
                pw_limit.pop('LIMIT')
                chars_used = 0
                for char_set in pw_limit:
                    for _ in range(pw_limit[char_set]):
                        user_pw += secrets.choice(list(PW_SET[char_set]))
                        chars_used += 1
                # calculate how many characters left user has
                chars_left = pw_length - chars_used
                # loop to generate and display user pw
                for _ in range(chars_left):
                    char_type = secrets.choice(list(PW_SET))
                    user_pw += secrets.choice(PW_SET[char_type])
                pw_list = list(user_pw)
                numpy.random.shuffle(pw_list)
                user_pw_set = ''.join(pw_list)
            else:
                raise UnboundLocalError
        except ValueError:
            print("\t### Please try again.")
        except UnboundLocalError:
            print("\t### A strong password is between 12 "
                  "and 64 characters.")
        else:
            print('#' * 80)
            print('\t# The user password generated was:', user_pw_set)
            print('#' * 80)
            return pw_length


# function if user chooses for calculating a percentage
def calculate_percent():
    """
    function to calculate and formate a percentage
    :param: user_num, user_den, digits_out, calc_percent
    :except: if user enters something other than an integer
    :return: output display
    """
    # while loop until a valid answer is given
    calc_percent = 0
    while calc_percent == 0:
        # try-except for error handling
        try:
            print('#' * 80)
            user_num = int(input("\t--Please input the numerator: "))
            user_den = int(input("\t--Please input the denominator: "))
            if user_den != 0:
                digits_out = int(input("\t--Please input the number "
                                       "of decimal points :"))
                calc_percent = float((user_num / user_den) * 100)
            else:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print("\t### Cannot divide by zero.")
        except ValueError:
            print("\t### Please ensure that entries are whole numbers.")
        else:
            print(f"\t# The fraction {user_num}/{user_den} as a percentage"
                  f" is: {calc_percent:.{digits_out}f}%")
            print('#' * 80)


# function if user chooses to calculate days to specified date
def calculate_days():
    """
    function to calculate how many days from today until July 4, 2025
    :param: date_today, date_from, diff_days
    :return: None
    """
    date_today = datetime.today()
    date_from = datetime.strptime("07-04-2025", '%m-%d-%Y')
    diff_days = (date_from - date_today).days
    print('#' * 80)
    print(f"\t --There are {diff_days} days until July 4, 2025 from "
          f"today, {date_today:%B, %d, %Y}")
    print('#' * 80)


# function if user chooses to calculate a formula in a triangle
def calculate_triangle():
    """
    function to calculate the leg of a triangle using the Law of Cosines
    :param: side1, side2, side3, angle_c
    :except: if user inputs a value other than floats or integers
    :return: output display
    """
    # while loop until a valid answer is given
    side3 = 0
    while side3 == 0:
        # try-except for error handling
        try:
            print('#' * 80)
            side1 = float(input("\tPlease input the value for side 1: "))
            side2 = float(input("\tPlease input the value for side 2: "))
            angle_c = float(input("\tPlease input the value for angle C: "))
            side_a_b = (side1 ** 2) + (side2 ** 2)
            side_3_a = side_a_b - (2 * side1 * side2) * \
                       numpy.cos(numpy.radians(angle_c))
            side3 = math.sqrt(side_3_a)
        except ValueError:
            print("Please verify input.")
        else:
            print('-' * 80)
            print(f"\t--The formula for the Law of Cosines is "
                  f"c^2=a^2+b^2-2ab*cos(C).\n\t--Side A = {side1}"
                  f"\n\t--Side B = {side2}\n\t--Using the Law of "
                  f"Cosines, the calculated side is: {side3:.2f}")
            print('#' * 80)


# function if user chooses to calculate volume
def calculate_vol():
    """
    function to calculate the volume of a right circular cylinder
    :param: know_value, cyl_circumference, cyl_radius,
        cyl_height, cyl_volume
    :except: if user enters something other than a float
        or enters something other than radius or circumference.
    :return: output display
    """
    # while loop until a valid answer is given
    cyl_volume = 0
    while cyl_volume == 0:
        try:
            valid_values = ['circumference', 'c', 'r', 'radius']
            known_value = str(input("\t--Do you know the radius or "
                                    "the circumference? ").lower())
            if known_value in valid_values:
                if known_value in ['circumference', 'c']:
                    cyl_circumference = float(input("\tPlease input "
                                                    "the circumference of "
                                                    "the cylinder: "))
                    cyl_radius = cyl_circumference / (2 * math.pi)
                elif known_value in ['radius', 'r']:
                    cyl_radius = float(input("\t--Please input the "
                                             "radius of the cylinder: "))
                    cyl_circumference = (2 * math.pi) * cyl_radius
            else:
                raise ValueError
            cyl_height = float(input("\t--Please input the height of"
                                     " the cylinder: "))
            cyl_volume = (math.pi * (cyl_radius ** 2) * cyl_height)
        except ValueError:
            print("--Please verify input.")
        else:
            print('-' * 80)
            print(f"\t--The formula for the Volume of a Right Cylinder"
                  f" is pi*r^2*h.\n\t--Circumference = {cyl_circumference:.2f}"
                  f"\n\t--Radius = {cyl_radius:.2f}\n\t--Height = {cyl_height}"
                  f"\n\t--The volume of the cylinder is {cyl_volume:.2f}")
            print('#' * 80)


# runs main program
if __name__ == "__main__":
    main()
