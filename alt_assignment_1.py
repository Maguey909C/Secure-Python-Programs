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
        return False
    else:
        if response.upper() not in all_states:
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
        return False
    else:
        if response.upper() not in us_names:
            return False
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
            return True
        else:
            return False
    else:
        return False


def voting_questions(subject):
    """
    INPUT: A subject to prompt the user
    OUTPUT: A valid response based on the question that will be used in the summary function
    """
    response = question(subject)
    str_categories = ["first_name", "last_name"]
    while True:
        if subject in str_categories:
            if check_name(response):
                return response
            else:
                print(error_prompt())
                break
        elif subject == 'age':
            if check_age(response):
                return response
            else:
                print(error_prompt())
                break
        elif subject == 'citizenship':
            if check_citizenship(response):
                return response
            else:
                print(citizenship_prompt())
                break
        elif subject == 'state':
            if check_state(response):
                return response
            else:
                print("Please use a valid abbreviation for your state. Example: California = CA.")
                break
        else:
            if check_zip(response):
                return response
            else:
                print(error_prompt())
                break


def user_interest(response):
    """
    INPUT: String response from user
    OUTPUT: Validated whether or not this makes sense
    """
    while True:
        user_input = input('Do you want to continue with Voter Registration? [y/n] ').strip()
        if user_input == 'y':
            return response
        elif user_input == 'n':
            return False
        else:
            print("Oops. That is not a valid entry. Try again plz.")


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
    else:
        print("There is an issue with your entries. Plz try again.")
        return False


if __name__ == '__main__':
    print(start_prompt())
    while True:
        SELECTION = input('Do you want to continue with Voter Registration? [y/n] ').strip()
        if SELECTION == 'y' or SELECTION == 'yes':
            FIRST_NAME = user_interest(voting_questions("first_name"))
            LAST_NAME = user_interest(voting_questions("last_name"))
            AGE = user_interest(voting_questions('age'))
            CITIZENSHIP = user_interest((voting_questions('citizenship')))
            STATE = user_interest(voting_questions("state"))
            ZIPCODE = user_interest(voting_questions("zipcode"))
            print(summary(FIRST_NAME, LAST_NAME, AGE, CITIZENSHIP, STATE, ZIPCODE))
            print(end_prompt())
            break
        elif SELECTION == 'n' or SELECTION == 'no':
            break
        else:
            print("Oops! That is not a valid entry. Please enter yes (y) or no (n).")
    print("Goodbye")
