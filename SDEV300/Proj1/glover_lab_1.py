"""
_filename: "glover_lab_1.py
_coursename: "SDEV300 6382"
_author: "Corey Glover"
_copyright: "None"
_credits: ["Corey Glover", "Craig Poma"]
_license: "GPL"
_version: "1.0.0"
_maintainer: "Corey Glover"
_email: "corey.j.glover@student.umgc.edu"
_description: "This program asks the user if they would like to use the
    voter Registration and if yes continues through other onscreen questions."
"""
import sys
import re

US_STATES = dict({
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming'
})


class UserError(Exception):
    """
    General exception when an error is found from user input. Message displayed in exception.
    """


class VerifyError(Exception):
    """
    Exception to verify that user input is correct
    """


class AgeError(Exception):
    """
    A catch for user age being over a specified number
    """


def program_continue():
    """
    Asks if user wishes to continue. If so it continues the program, if not
    it will exit.
    :param: valid_inputs, register
    :exception: user chooses to exit by entering no variation
    """
    valid_inputs = ['y', 'yes', 'n', 'no']
    register = None

    while register not in valid_inputs:
        register = str(input("Would you like to continue registration, yes/no? ").lower())
        if register not in valid_inputs:
            print("\tPlease enter yes or no.")
    if register in ['n', 'no']:
        print('-' * 20)
        print("Thank you for using the Voter Registration Application, "
              "you have chosen to exit.")
        print('-' * 20)
        sys.exit()


def main():
    """
    The main function of the program. Calls each function and prints inputs
    """
    print('-' * 20)
    print("Welcome to the Voter Registration Application")

    program_continue()
    citizenship = user_citizen()
    program_continue()
    age = user_age()
    program_continue()
    name = user_name()
    program_continue()
    state = user_state()
    program_continue()
    zipcode = user_zipcode()

    print("Thank you for registering to vote! Here is the information entered:"
          "\n\n\t#########################################################")
    print("\t# Name(First Last): ", name.title(), "\n\t# Age: ", age,
          "\n\t# U.S. Citizen: ", citizenship.upper(), "\n\t# State: ", state.upper(),
          "\n\t# Zipcode:", zipcode)
    print("\t#########################################################\n")
    print('-' * 20)
    print('Thank you for using the Voter Registration Application.'
          '\nYour voter registration card should be available within 7-10 business days.')
    print('-' * 20)
    sys.exit()


def user_name():
    """
    This function asks the user first_name, last_name then combines them.
    :param: first_name, last_name, name
    :exception: if username isn't alphabetic or is blank
    :return: name
    """
    while True:
        try:
            first_name = str(input("\tEnter your First Name: "))
            if re.match('^[A-Za-z]{,30}$.*', first_name):
                program_continue()
                last_name = str(input("\tEnter your Last Name: "))
                if re.match('^[\'A-Za-z]+(-[\'A-Za-z])$.*', last_name):
                    name = first_name + str(" ") + str(last_name)
                else:
                    raise ValueError
            else:
                raise ValueError
        except ValueError:
            print("###Please verify entered name.###")
        else:
            return name


def user_age():
    """
    This function to ask user age then checks it is between 18 and 120.
    :param: age, verify_age, verified_inputs
    :exception: if user is under 18 or over 120 or enters something other than integer
    :return: age
    """
    while True:
        try:
            age = int(input("\tPlease enter age: "))
            if age < 18:
                raise UserError
            if age > 105:
                raise AgeError
        except AgeError:
            print("You entered an age of: ", age)
            verify_age = str(input("\t###Was the age correctly "
                                   "entered, yes/no?### ").lower())
            if verify_age in ['y', 'yes']:
                print("Thank you for verifying.")
                break
        except UserError:
            print("\tYou must be over the age of 18 to register.")
            sys.exit()
        except ValueError:
            print("\t###Please verify age entered.###")
        else:
            return age


def user_citizen():
    """This function verifies that user is a U.S. Citizen.
    :param: valid_citizen, citizenship
    :exception: if user enters anything other than variation of yes
    :return: citizenship
    """
    while True:
        try:
            valid_citizen = ['y', 'yes']
            citizenship = str(input("\tAre you a U.S. Citizen? yes/no: ").lower())

            if citizenship in ['n', 'no']:
                raise UserError
            if citizenship not in valid_citizen:
                raise VerifyError
        except VerifyError:
            print("\tPlease enter yes or no.")
        except UserError:
            print("\tERROR: Sorry, U.S. Citizenship required to register.")
            sys.exit()
        else:
            return citizenship


def user_state():
    """
    This function to ask user for their state of residency
    :param: state
    :exception: if user stat entered isn't in the dictionary
    :return: state
    """
    while True:
        try:
            state = input("\tEnter your State of Residency(eg. Texas = TX): ").upper()

            if state not in US_STATES or len(state) != 2:
                raise UserError
        except UserError:
            print("###Please verify state of residency(Format in (eg. Texas = TX).###")
        else:
            return state


def user_zipcode():
    """
    This function asks the user for their zipcode
    :param: zipcode
    :exception: if zipcode doesn't = 5 digits or 9 digits and isn't between 501 and 99950
    :return: zipcode
    """
    while True:
        try:
            zipcode = input("\tPlease enter your zipcode: ")
            if not re.fullmatch('^[0-9]{5}(?:-[0-9]{4})?$', zipcode):
                raise UserError
        except UserError:
            print("###Please verify zipcode.###")
        else:
            return zipcode


if __name__ == "__main__":
    main()
