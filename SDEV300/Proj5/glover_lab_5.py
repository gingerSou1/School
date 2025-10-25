"""
_filename: "glover_lab_5.py
_course name: "SDEV300 6382"
_author: "Corey Glover"
_copyright: "None"
_credits: ["Corey Glover"]
_license: "GPL"
_version: "1.0.0"
_maintainer: "Corey Glover"
_email: "corey.j.glover@student.umgc.edu"
_description: "This program will take data then display a graph"
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

POP_DF = pd.read_csv(r'C:\Users\Corey\Desktop\PythonApps\Week5\PopChange.csv')
HOUSE_DF = pd.read_csv(r'C:\Users\Corey\Desktop\PythonApps\Week5\Housing.csv')


# main program
def main():
    """
    main program function
    :return:
    """
    user_menu()


def user_menu():
    """
    function that displays user menu
    :param: choice
    :return: N/A
    """
    # print menu
    choice = ''
    while choice != '0':
        print('*' * 10, "Welcome to the Python Data Analysis App", '*' * 10)
        print("\t### -MAIN MENU- ###")
        print("Select the file you want to analyze:")
        print("""
                    \t1: Population Data
                    \t2: Housing Data
                    \t0: Exit the Program
                    """)
        print("*******************************")
        # handle user choice of menu items
        choice = str(input("Please select an item: ").upper())
        if choice == '1':
            population_data()
        elif choice == '2':
            housing_data()
        elif choice == '0':
            print("\t# Thank you for using the program!")
            sys.exit()
        else:
            print("\t### That is not a valid input! ###")


def population_data():
    """
    function that gets population data
    :param: choice
    :except: If user enters values not acceptable
    :return: N/A
    """
    choice = ''
    while choice != 0:
        print('*' * 80)
        print("""\t### -YOU'RE IN POPULATION DATA- ###
              \nSelect the Column you want to analyze:
              \t A: Population Apr 1
              \t B: Population Jul 1
              \t C: Change Population
              \t 0: Exit Population Menu""")
        # handle user choice of menu items
        choice = str(input("Please select an item: ").upper())
        if choice == 'A':
            pop_apr()
        elif choice == 'B':
            pop_jul()
        elif choice == 'C':
            pop_change()
        elif choice == '0':
            print('\t# Back to main menu.')
            break
        else:
            print('\t### That is not a valid input! ###')


def pop_apr():
    """
    function that display's the population on Apr 1 and graph
    :return:
    """
    print(f'\t# The count is {POP_DF["Pop Apr 1"].count()}.'
          f'\n\t# The mean is {np.mean(POP_DF["Pop Apr 1"])}.'
          f'\n\t# The Min is {np.min(POP_DF["Pop Apr 1"])}.'
          f'\n\t# The Max is {np.max(POP_DF["Pop Apr 1"])}.')
    plt.title('April 1 Population')
    plt.xlabel('Total Population')
    plt.ylabel('Sample Quantity')
    plt.subplots_adjust(bottom=.25, left=.25)
    plt.axis('on')
    plt.grid(True)
    plt.hist(POP_DF['Pop Apr 1'], bins=50, edgecolor='black')
    plt.show()


def pop_jul():
    """
    function to display population on July 1 and graph
    :return:
    """
    print(f'\t# The count is {POP_DF["Pop Jul 1"].count()}.'
          f'\n\t# The mean is {np.mean(POP_DF["Pop Jul 1"])}.'
          f'\n\t# The Min is {np.min(POP_DF["Pop Jul 1"])}.'
          f'\n\t# The Max is {np.max(POP_DF["Pop Jul 1"])}.')
    plt.title('July 1 Population')
    plt.xlabel('Total Population')
    plt.ylabel('Sample Quantity')
    plt.subplots_adjust(bottom=.25, left=.25)
    plt.axis('on')
    plt.grid(True)
    plt.hist(POP_DF['Pop Jul 1'], bins=50, edgecolor='black')
    plt.show()


def pop_change():
    """
    function to display change of population and graph
    :return:
    """
    print(f'\t# The count is {POP_DF["Change Pop"].count()}.'
          f'\n\t# The mean is {np.mean(POP_DF["Change Pop"])}.'
          f'\n\t# The Min is {np.min(POP_DF["Change Pop"])}.'
          f'\n\t# The Max is {np.max(POP_DF["Change Pop"])}.')
    plt.title('Change of Population')
    plt.xlabel('Total Population')
    plt.ylabel('Sample Quantity')
    plt.subplots_adjust(bottom=.25, left=.25)
    plt.axis('on')
    plt.grid(True)
    plt.hist(POP_DF['Change Pop'], bins=50, edgecolor='black')
    plt.show()


def housing_data():
    """
    function that gets housing data
    :param: choice
    :except: If entered values not correct
    :return: N/A
    """
    choice = ''
    while choice != 0:
        try:
            print('*' * 80)
            print("""\t### -YOU'RE IN HOUSING DATA- ###.
                  \nSelect the Column you want to analyze:
                  \t A: Age
                  \t B: Bedrooms
                  \t C: Year Built
                  \t D: Rooms
                  \t E: Utility
                  \t 0: Exit Housing Menu""")
            # handle user choice of menu items
            choice = str(input("Please select an item: ").upper())
            if choice == 'A':
                house_age()
            elif choice == 'B':
                house_bdrms()
            elif choice == 'C':
                house_built()
            elif choice == 'D':
                house_rooms()
            elif choice == 'E':
                house_utility()
            elif choice == '0':
                print('\t# Back to main menu.')
                break
            else:
                print('\t### That is not a valid input! ###')
        except TypeError:
            print('Please try again.')


def house_age():
    """
    function to display age of house and graph
    :return:
    """
    print(f'\t# The count is {HOUSE_DF["AGE"].count()}.'
          f'\n\t# The mean is {np.mean(HOUSE_DF["AGE"])}.'
          f'\n\t# The Min is {np.min(HOUSE_DF["AGE"])}.'
          f'\n\t# The Max is {np.max(HOUSE_DF["AGE"])}.')
    plt.title('Age of Houses')
    plt.xlabel('Age of House in Years')
    plt.ylabel('Number of Houses')
    plt.subplots_adjust(bottom=.25, left=.25)
    plt.axis('on')
    plt.grid(True)
    plt.hist(HOUSE_DF['AGE'], bins=50, edgecolor='black')
    plt.show()


def house_bdrms():
    """
    function to display house bedrooms and graph
    :return:
    """
    print(f'\t# The count is {HOUSE_DF["BEDRMS"].count()}.'
          f'\n\t# The mean is {np.mean(HOUSE_DF["BEDRMS"])}.'
          f'\n\t# The Min is {np.min(HOUSE_DF["BEDRMS"])}.'
          f'\n\t# The Max is {np.max(HOUSE_DF["BEDRMS"])}.')
    plt.title('Total Bedrooms')
    plt.xlabel('Number of Bedrooms')
    plt.ylabel('Number of Houses')
    plt.subplots_adjust(bottom=.25, left=.25)
    plt.axis('on')
    plt.grid(True)
    plt.hist(HOUSE_DF['BEDRMS'], bins=50, edgecolor='black')
    plt.show()


def house_built():
    """
    function to display year built and graph
    :return:
    """
    print(f'\t# The count is {HOUSE_DF["BUILT"].count()}.'
          f'\n\t# The mean is {np.mean(HOUSE_DF["BUILT"])}.'
          f'\n\t# The Min is {np.min(HOUSE_DF["BUILT"])}.'
          f'\n\t# The Max is {np.max(HOUSE_DF["BUILT"])}.')
    plt.title('Year House Built')
    plt.xlabel('Year Built')
    plt.ylabel('Number of Houses')
    plt.subplots_adjust(bottom=.25, left=.25)
    plt.axis('on')
    plt.grid(True)
    plt.hist(HOUSE_DF['BUILT'], bins=50, edgecolor='black')
    plt.show()


def house_rooms():
    """
    function to display number of rooms and graph
    :return:
    """
    print(f'\t# The count is {HOUSE_DF["ROOMS"].count()}.'
          f'\n\t# The mean is {np.mean(HOUSE_DF["ROOMS"])}.'
          f'\n\t# The Min is {np.min(HOUSE_DF["ROOMS"])}.'
          f'\n\t# The Max is {np.max(HOUSE_DF["ROOMS"])}.')
    plt.title('Number of Total Rooms')
    plt.xlabel('Total Rooms')
    plt.ylabel('Number of Houses')
    plt.subplots_adjust(bottom=.25, left=.25)
    plt.axis('on')
    plt.grid(True)
    plt.hist(HOUSE_DF['ROOMS'], bins=50, edgecolor='black')
    plt.show()


def house_utility():
    """
    function to display utility and graph
    :return:
    """
    print(f'\t# The Count is {HOUSE_DF["UTILITY"].count()}.'
          f'\n\t# The Mean is {np.mean(HOUSE_DF["UTILITY"])}.'
          f'\n\t# The Minimum is {np.min(HOUSE_DF["UTILITY"])}.'
          f'\n\t# The Maximum is {np.max(HOUSE_DF["UTILITY"])}.')
    plt.title('Total Cost of Utilities')
    plt.xlabel('Utilities(in $)')
    plt.ylabel('Number of Houses')
    plt.subplots_adjust(bottom=.25, left=.25)
    plt.axis('on')
    plt.grid(True)
    plt.hist(HOUSE_DF['UTILITY'], bins=50, edgecolor='black')
    plt.show()


# runs main program
if __name__ == "__main__":
    main()
