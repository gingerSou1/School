"""
_filename: "glover_lab_4.py
_course name: "SDEV300 6382"
_author: "Corey Glover"
_copyright: "None"
_credits: ["Corey Glover"]
_license: "GPL"
_version: "1.0.0"
_maintainer: "Corey Glover"
_email: "corey.j.glover@student.umgc.edu"
_description: ""
"""
import ast
import re
import numpy as np


# main program
def main():
    """
    main program function
    :return:
    """
    # ask user to play the game and whenever run is complete asks again
    game_continue = ''
    print("*" * 10, "Welcome to the Python Matrix Application", '*' * 10)
    while game_continue not in ['n', 'no']:
        try:
            # ask user if they would like to use the app
            print("# Do you want to play the Matrix Game?")
            game_continue = str(input("\t# Enter Y for Yes or"
                                      " N for No: ").lower())
            # if yes run phone function then zip function
            if game_continue in ['y', 'yes']:
                try_again = 'y'
                while try_again in ['y', 'yes']:
                    phone_num = user_phone()
                    user_zip = user_zipcode()
                    print(f'\t# The users phone number is {phone_num} and '
                          f'their zipcode is {user_zip}.')
                    try_again = str(input("Would you like to enter phone "
                                          "and zipcode again? y/n ").lower())
                # print user phone and zip then run matrix functions
                    if try_again in ['n', 'no']:
                        matrix_menu()
                    else:
                        print("\t# Invalid entry.")
                        try_again = str(input("Would you like to enter "
                                              "phone and zipcode again? "
                                              "y/n ").lower())
                # if no then exit
            elif game_continue in ['n', 'no']:
                print('*' * 80)
                print("### Thank you for using the application. ###")
            else:
                raise ValueError
        except ValueError:
            print("### Please verify input. ###")
            game_continue = ''


def user_phone():
    """
    This function asks the user for their phone number
    :param: phone_num
    :exception: if phone number isn't in format or not integer
    :return: phone_num
    """
    while True:
        try:
            # ask user for phone number in format.
            # regex accepts other formats than one listed.
            phone_num = input("\t# Please enter your phone number"
                              "(format: xxx-xxx-xxxx): ")
            # if input doesn't match regex then throw error
            if not re.fullmatch(r'^(\([0-9]{3}\)?|[0-9]{3}-)'
                                r'[0-9]{3}-[0-9]{4}$', phone_num):
                raise TypeError
        except TypeError:
            print("\t### Please verify phone number format. ###")
        else:
            return phone_num


def user_zipcode():
    """
    This function asks the user for their zipcode
    :param: user_zip
    :exception: if zipcode doesn't =  9 digits and isn't between 501 and 99950
    :return: user_zip
    """
    while True:
        try:
            # ask user for zipcode and if not in regex
            # specified format throw error
            user_zip = input("\t# Please enter your zipcode"
                             "(format: xxxxx-xxxx): ")
            if not re.fullmatch(r'^[0-9]{5}(?:-[0-9]{4})?$', user_zip):
                raise TypeError
        except TypeError:
            print("\t### Please verify zipcode. ###")
        else:
            return user_zip


def matrix_menu():
    """
    function to get user choice of operation to perform on matrix entered
    :param: first_matrix, second_matrix, choice, add_matrix, sub_matrix
    matrix_transpose, multi_matrix, multi_matrix_ele
    :return: None
    """
    change_matrix = 'yes'
    while change_matrix in ['yes', 'y']:
        try:
            # call user matrix functions then assign to
            # variables.
            first_matrix = user_matrix_1()
            second_matrix = user_matrix_2()
            # print menu
            print('*' * 80)
            print("Select a Matrix Operation from below: ")
            print("""
            \t1: Addition
            \t2: Subtraction
            \t3: Multiplication
            \t4: Element by Element Multiplication
            """)
            print("*******************************")
            # handle user choice of menu items
            choice = input("Please select an item: ")
            if choice == '1':
                add_matrix = matrix_add(first_matrix, second_matrix)
                matrix_transpose = np.transpose(add_matrix)
                mean_row = add_matrix.mean(0)
                mean_col = add_matrix.mean(1)
                print(f"#The transpose is \n{matrix_transpose}."
                      f"\nThe row mean is {mean_row}"
                      f"\nThe column mean is {mean_col}")
            elif choice == '2':
                sub_matrix = matrix_sub(first_matrix, second_matrix)
                matrix_transpose = np.transpose(sub_matrix)
                mean_row = sub_matrix.mean(0)
                mean_col = sub_matrix.mean(1)
                print(f"# The transpose is \n{matrix_transpose}."
                      f"\n# The row mean is {mean_row}"
                      f"\n# The column mean is {mean_col}")
            elif choice == '3':
                multi_matrix = matrix_multi(first_matrix, second_matrix)
                matrix_transpose = np.transpose(multi_matrix)
                mean_row = multi_matrix.mean(0)
                mean_col = multi_matrix.mean(1)
                print(f"# The transpose is \n{matrix_transpose}."
                      f"\n# The row mean is {mean_row}"
                      f"\n# The column mean is {mean_col}")
            elif choice == '4':
                multi_matrix_ele = matrix_ele_multi(first_matrix,
                                                    second_matrix)
                matrix_transpose = np.transpose(multi_matrix_ele)
                mean_row = multi_matrix_ele.mean(0)
                mean_col = multi_matrix_ele.mean(1)
                print(f"# The transpose is \n{matrix_transpose}."
                      f"\n# The row mean is {mean_row}"
                      f"\n# The column mean is {mean_col}")
            # else asking if user wants to enter another set of
            # matrix numbers. If no return to main program.
            change_matrix = str(input("Do you want to enter another set of "
                                      "matrices? y/n ").lower())
            if change_matrix in ['yes', 'y'] or \
                    change_matrix in ['no', 'n']:
                if change_matrix in ['yes', 'y']:
                    matrix_menu()
                elif change_matrix in ['no', 'n']:
                    break
            else:
                print("Not a valid response. Please re-enter matrix values.")
                matrix_menu()
        except TypeError:
            print("Please try again.")


def user_matrix_1():
    """
    function to get user generated matrix
    :param: user_input_array1, array_1, first_matrix
    :except: if user enters value other than int
    :return: user_matrix
    """
    while True:
        try:
            # ask user for 9 numbers separated by comma
            print("\t# Please enter your first 3x3 matrix values separated "
                  "by commas(9 integers): ")
            # set user input to numpy array
            array_1 = np.array(ast.literal_eval(input()))
            # reshape array in a 3x3 format
            first_matrix = array_1.reshape((3, 3))
        # error handling
        except NameError:
            print("\t### Please ensure 3x3 matrix values separated by commas"
                  "(9 integers total) and are numbers! Try again. ###")
        except SyntaxError:
            print("\t### Please ensure 3x3 matrix values separated by commas"
                  "(9 integers total) and are numbers! Try again. ###")
        else:
            return first_matrix


def user_matrix_2():
    """
    function to get user generated matrix
    :param: user_input_array2, array_2, second_matrix
    :except: if user enters value other than int
    :return: second_matrix
    """
    while True:
        try:
            # ask user for matrix input
            print("\t# Please enter your second 3x3 matrix values separated "
                  "by commas(9 integers): ")
            # take user input and assign to numpy array
            array_2 = np.array(ast.literal_eval(input()))
            # set array to 3x3 matrix
            second_matrix = array_2.reshape((3, 3))
        # error handling
        except NameError:
            print("\t### Please ensure 3x3 matrix values separated by commas"
                  "(9 integers total) and are numbers! Try again. ###")
        except SyntaxError:
            print("\t### Please ensure 3x3 matrix values separated by commas"
                  "(9 integers total) and are numbers! Try again. ###")
        else:
            return second_matrix


def matrix_add(first_matrix, second_matrix):
    """
    function that takes user input for matrix and adds them
    together
    :param: mat_add, first_matrix, second_matrix
    :return: matrix_added
    """
    # takes user inputs then performs addition
    mat_add = np.add(first_matrix, second_matrix)
    print(f'# The first matrix entered was: \n'
          f'{first_matrix}\n# The second matrix'
          f' entered was\n{second_matrix}\n'
          f'# The sum of the two matrix is:\n'
          f'{mat_add}')
    return mat_add


def matrix_sub(first_matrix, second_matrix):
    """
    function that takes user input for matrices and subs them
    :param: mat_sub, first_matrix, second_matrix
    :return: matrix_sub
    """
    # takes user inputs then performs subtraction
    mat_sub = np.subtract(first_matrix, second_matrix)
    print(f'# The first matrix entered was: \n'
          f'{first_matrix}\n# The second matrix'
          f' entered was\n{second_matrix}\n'
          f'# The difference of the two matrix is:\n'
          f'{mat_sub}')
    return mat_sub


def matrix_ele_multi(first_matrix, second_matrix):
    """
    function that takes user input for matrices and multiplies
    the elements
    :param: mat_multi_ele, first_matrix, second_matrix
    :return: matrix_elements
    """
    # takes user inputs then performs multiplication
    mat_multi_ele = np.multiply(first_matrix, second_matrix)
    print(f'# The first matrix entered was: \n'
          f'{first_matrix}\n# The second matrix'
          f' entered was\n{second_matrix}\n'
          f'# The two values multiplied is:\n'
          f'{mat_multi_ele}')
    return mat_multi_ele


def matrix_multi(first_matrix, second_matrix):
    """
    function that takes user input for matrices and multiplies
    them
    :param: mat_multi, first_matrix, second_matrix
    :return: matrix_multi
    """
    # takes user inputs then performs multiplication by elements
    mat_multi = np.matmul(first_matrix, second_matrix)
    print(f'# The first matrix entered was: \n'
          f'{first_matrix}\n# The second matrix'
          f' entered was\n{second_matrix}\n'
          f'# The two values with the elements multiplied is:\n'
          f'{mat_multi}')
    return mat_multi


# runs main program
if __name__ == "__main__":
    main()
