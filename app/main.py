import os


def run_program():
    """
    ---------------------help---------------------
    | -->   you can use "res" to show the result |
    |   of data and use "per" to enter your      |
    |   considered percentage and get grade      |
    | -->   you can quit program by enter "q"    |
    ----------------------------------------------
    """
    answer = input('-->')
    if answer == 'q':
        print('\t'*2 + 'Goodbye...!')
        return
    elif answer == 'res':
        os.system('python result.py')
    elif answer == 'per':
        os.system('python percentage.py')
    else:
        run_program()


run_program()
