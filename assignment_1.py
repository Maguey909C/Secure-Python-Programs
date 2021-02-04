#!/usr/bin/env python3
# CS202 Project 1: Voting Machine
# @version 2021/01/16
# @author Chase Renick
"""
Program tells if someone qualifies for voter registration or not while handling exceptions.
"""
import re


def start_prompt():
    """
    INPUT: None
    OUTPUT: Prompt when user starts voter registration program
    """
    return """
    Welcome to the Python Voter Registration Application.
    """


def end_prompt():
    """
    INPUT: None
    OUTPUT: Prompt when user is finished using voter registration program
    """
    return """
    Thanks for trying the Voter Registration Application.  
    Your voter registration card should be shipped within 3 weeks.
    """


def error_prompt():
    """
    INPUT: None
    OUTPUT: Generic error prompt when user types in an invalid entry
    """
    return """That is not a valid entry. Try again."""


def citizenship_prompt():
    """
    INPUT: None
    OUTPUT: Prompt for when user is not a US citizen
    """
    return ("It appears you have entered an invalid value or are not a US citizen.\n"
            "Voter registration is only for qualified US citizens.\n")


def question(subject):
    """
    INPUT: None
    OUTPUT: Prompt for when user wants to input something in program
    """
    return str(input("What is your " + subject + "? ")).strip()

def user_decision():
    """
    INPUT: None
    OUTPUT: User decision if they want to continue with the program or not
    """
    return input('Do you want to continue with Voter Registration? [y/n] ').strip()

def contains_numbers(response):
    """
    INPUT: A string of user input
    OUTPUT: A boolean value if it is has numbers or not
    """
    return bool(re.search(r'\d', response))


def contains_special(response):
    """
    INPUT: A string of user input
    OUTPUT: A boolean value if it is has numbers or not
    """
    return bool(re.search(r'[@_!#$%^&*()<>?/\|}{~:]', response))


def contains_letters(response):
    """
    INPUT: A string of user input
    OUTPUT: A boolean value if it is has numbers or not
    """
    return bool(re.search(r'[A-Za-z]', response))


def check_name(response):
    """
    INPUT: A string
    Output: A boolean if it follows the rules
    """
    if contains_numbers(response) or \
            contains_special(response) or \
            len(response) < 2 or \
            len(response) >= 15:
        return False
    else:
        return True


def check_age(response):
    """
    INPUT: User's input
    Output: A boolean if it follows the rules of an integer
    """
    if contains_letters(response) or \
            contains_special(response) or \
            len(response) > 3:
        return False
    else:
        try:
            response = float(response)
            if response in range(18, 120):
                print("Great! Looks like you are eligible to vote.")
                return True
            elif response in range(0, 17):
                print("Looks like you are too young to vote...")
                return False
            else:
                return False
        except ValueError:
            print("There is a value error in your response. Please revise")


def check_state(response):
    """
    INPUT: User's input
    OUTPUT: validating if the state selected is actually real
    """
    all_states = ['AK', 'AL', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE',
                  'FL', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY',
                  'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MP', 'MS', 'MT',
                  'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK',
                  'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UM', 'UT',
                  'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY']
    if contains_numbers(response) or contains_special(response) or len(response) != 2:
        print("It appears you entered something other than a state. Start over.")
        return False
    else:
        if response.upper() not in all_states:
            print("It appears you have entered an invalid US state. Please try again.")
            return False
        return True


def check_citizenship(response):
    """
    INPUT: User's input
    OUTPUT: validating if the citizenship is real selected is actually real
    """
    us_names = ["US", "UNITED STATES", "USA", "UNITED STATES OF AMERICA", "US OF A", "AMERICA"]
    if contains_numbers(response) or \
            contains_special(response) or \
            len(response) >= 25 or \
            len(response) < 2:
        print("It appears you entered something other than a valid country. Please start again.")
        return False
    else:
        if response.upper() not in us_names:
            print("You are not from the US or have entered an invalid entry. Please try again.")
            return False
        print("You indicated that you are a US citizen.")
        return True


def check_zip(response):
    """
    INPUT: User's input
    Output: A boolean if it follows the rules of a zipcode
    """
    if not contains_letters(response) and \
            not contains_special(response) and \
            len(response) == 5:
        response = float(response)
        if response in range(10000, 99999):
            print("Great looks like you entered a valid zipcode! You are almost done.")
            return True
        else:
            print("It seems you have entered an invalid zipcode. Please try again.")
            return False
    else:
        return False


def summary(first_name, last_name, age, citizenship, state, zipcode):
    """
    INPUT: First name, last name, age, citizenship, state, zipcode of applicant
    OUTPUT: A summary of this information to user to let them know it was received
    """
    if check_name(first_name) and \
            check_name(last_name) and \
            check_age(age) and \
            check_state(state) and \
            check_citizenship(citizenship) and \
            check_zip(zipcode):
        print("Thanks for registering to vote. Here is the information we received:")
        print("Name (first, last):", first_name + " " + last_name)
        print("Age:", age)
        print("U.S. Citizenship:", citizenship)
        print("State:", state)
        print("Zipcode:", zipcode)
        return True


if __name__ == '__main__':
    print(start_prompt())
    while True:
        # Ask user if they want to continue with voter registration
        SELECTION = user_decision()

        if SELECTION == 'y':
            RESPONSE_FNAME = question('first_name')
            if check_name(RESPONSE_FNAME) and SELECTION == 'y':
                FIRST_NAME = RESPONSE_FNAME
                SELECTION = user_decision()
                if SELECTION == 'y':
                    RESPONSE_LNAME = question('last_name')
                    if check_name(RESPONSE_LNAME) and SELECTION == 'y':
                        LAST_NAME = RESPONSE_LNAME
                        SELECTION = user_decision()
                        if SELECTION == 'y':
                            REPONSE_AGE = question("age")
                            if check_age(REPONSE_AGE) and SELECTION == 'y':
                                AGE = REPONSE_AGE
                                SELECTION = user_decision()
                                if SELECTION == 'y':
                                    RESPONSE_CITIZEN = question("citizenship")
                                    if check_citizenship(RESPONSE_CITIZEN) and SELECTION == 'y':
                                        CITIZENSHIP = RESPONSE_CITIZEN
                                        SELECTION = user_decision()
                                        if SELECTION == 'y':
                                            RESPONSE_STATE = question("state")
                                            if check_state(RESPONSE_STATE) and SELECTION == 'y':
                                                STATE = RESPONSE_STATE
                                                SELECTION = user_decision()
                                                if SELECTION == 'y':
                                                    RESPONSE_ZIP = question("zipcode")
                                                    if check_zip(RESPONSE_ZIP) and SELECTION == 'y':
                                                        ZIPCODE = RESPONSE_ZIP
                                                        print(summary(FIRST_NAME, LAST_NAME, AGE, CITIZENSHIP, STATE, ZIPCODE))
                                                        break
                                                    else:
                                                        print(error_prompt())
                                                        break
                                                elif SELECTION == 'n' or SELECTION == 'no':
                                                    break
                                                else:
                                                    print(error_prompt())
                                            else:
                                                print(error_prompt())
                                                break
                                        elif SELECTION == 'n' or SELECTION == 'no':
                                            break
                                        else:
                                            error_prompt()
                                    else:
                                        break
                                elif SELECTION == 'n' or SELECTION == 'no':
                                    break
                                else:
                                    print(error_prompt())
                            else:
                                error_prompt()
                                break
                        elif SELECTION == 'n' or SELECTION == 'no':
                            break
                        else:
                            print(error_prompt())
                    elif SELECTION == 'n' or SELECTION == 'no':
                        break
                    else:
                        print(error_prompt())
                elif SELECTION == 'n' or SELECTION == 'no':
                    break
                else:
                    print(error_prompt())
            elif SELECTION == 'n' or SELECTION == 'no':
                break
            else:
                print(error_prompt())
        elif SELECTION == 'n' or SELECTION == 'no':
            break
        else:
            print("Oops! That is not a valid entry. Please enter yes (y) or no (n).")
    print("Thanks for trying out the Voter Registration Program.")