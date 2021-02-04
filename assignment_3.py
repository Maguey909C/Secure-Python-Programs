#!/usr/bin/env python3
# CS300 Project 3: State Program
# @version 2021/01/29
# @author Chase Renick
"""
The master program prompts users about the particulars of
US states.  It can search for a state, produce a picture, and
change a population.
"""
import re
import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def start_prompt():
    """
    INPUT: None
    OUTPUT: Introduces purposes of program
    """
    return """Welcome to the Python State Program. \nProgram Options:\n"""


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


def not_contain_a_f(response):
    """
    Since initial options for users must be from a-f, g-z are not available. Regex checks user input
    :param response: User Input
    :return: A boolean value if a user's entry has
    """
    return bool(re.search(r'[F-Zf-z]', response))


def check_melange(response):
    """
    Checks multiple hack or incorrect attempts
    :param response: User input in response to a question
    :return: A boolean if they pass the meta checks
    """
    if contains_numbers(response) or \
            contains_special(response) or \
            response is None or \
            response == '' or \
            response not in all_states():
        return True
    else:
        return False


def select_state():
    """
    Asks the user for a state allowing them to
    enter a full name or an abbreviation.
    :return: Gives the details about the state from dictionary
    based on user input
    """
    user_input = input_function(
        "What state would you like details on? "
        "Please write out the name or abbreviation or full word: ") \
        .strip().lower()
    if not check_melange(user_input):
        if len(user_input) == 2:
            long_s = str(long_short()[user_input])
            return long_s, STATE_DETAILS[long_s]
        else:
            return user_input, STATE_DETAILS[user_input]
    else:
        print(error_prompt())
        return "Not Found", "Make sure you spelled the state or abbreviation correctly."


def check_answer(response):
    """
    Checks user response to what game they want to play
    response: A string
    :return: A boolean if it follows the rules
    """
    if contains_numbers(response) or \
            contains_special(response) or \
            not_contain_a_f(response) or \
            len(response) != 1:
        return False
    else:
        return True


def check_population(response):
    """
    Checks whether user types in a number
    or is trying to do something else
    response: A string
    :return: A boolean if it follows the rules
    """
    if contains_letters(response) or \
            contains_special(response) or \
            len(response) >= 12:
        return False
    else:
        return True


def lower_everything(a_string):
    """
    Function lowers everything is a given list
    :x: A list of strings
    :return: returns a list with string lowered strings
    """
    return list(map(str.lower, a_string))


def clean_print(nested_dictionary):
    """
    Function prints out the key value pairs of
    :return: prints out the key value pair
    for the nested dictionary
    and returns a string
    """
    summary = [(key, value) for key, value in nested_dictionary.items()]
    print(summary)
    return "List does not incorporate US territories or districts."


def long_s_name(nested_dictionary):
    """
    Function takes a nested dictionary goes
    through values then a key and lowers them
    so users can have full name of state
    :nested_dictionary: a nested dictionary
    with a key called acronym
    :return: Function returns a lowered list
    based on nested dictionary acronym
    """
    return lower_everything([key for key, value in nested_dictionary.items()])


def short_s_name(nested_dictionary):
    """
    Function takes a nested dictionary
    goes through values then a key called
    acronym to get the abbreviation for a state
    :nested_dictionary: a nested
    dictionary with a key called acronym
    :return: Function returns a lowered
    list based on nested dictionary acronym
    """
    return lower_everything(value['Acronym'] for key, value in nested_dictionary.items())


def long_short():
    """
    Function creates a dictionary of
    long state names and abbreviations
    :return: A nested dictionary of
    long short names
    """
    return dict(zip(short_s_name(STATE_DETAILS), long_s_name(STATE_DETAILS)))


def all_states():
    """
    Function takes acroynms and full
    names of all states, lowers them, and puts them
    in a list to be compared if user
    has typed in a real state
    :return: A nested dictionary of long short names
    """
    return lower_everything(short_s_name(STATE_DETAILS) + long_s_name(STATE_DETAILS))


def all_populations(nested_dictionary):
    """
       Function takes a nested dictionary goes
       through values then a key called
       acronym to get the abbreviation for a state
       :nested_dictionary: a nested dictionary
       with a key called population
       :return: Function returns a list of
       integer values for the population
       """
    return [int(value['Population']) for key, value in nested_dictionary.items()]


def find_state(specific_population):
    """
       Function tfinds a specific state
       based on a population
       :specific_population: Takes in a population
       :return: the state where that
       population is held
       """
    return [key for key, value in STATE_DETAILS.items()
            if value['Population'] == str(specific_population)]


def population_update():
    """
    Generates a randomized password based on
    a user specified length
    :return: A joined string based on the
    randomly selected numbers and characters
    """
    user_input = input_function(
        "What state would you like change population? "
        "Please write out the name or abbreviation or full word: ") \
        .strip().lower()
    if not check_melange(user_input):
        if len(user_input) == 2:
            long_s = str(long_short()[user_input])
            user_input2 = input_function("What is the new population? ").strip()
            if check_population(user_input2):
                print(long_s.upper())
                STATE_DETAILS[long_s]['Population'] = user_input2
                return STATE_DETAILS[long_s]
            else:
                return error_prompt()
        else:
            user_input2 = input_function("What is the new population? ").strip()
            if check_population(user_input2):
                print(user_input.upper())
                STATE_DETAILS[user_input]['Population'] = user_input2
                return STATE_DETAILS[user_input]
            else:
                return error_prompt()
    else:
        print(error_prompt())
        return "Make sure you spelled the state or abbreviation correctly."


def game_selection(response):
    """
    :param response: User's selection for
    the program they wish to execute
    :return: A boolean, but also prints out
    the results of one of the selected programes
    """
    if response == 'a':
        print(clean_print(STATE_DETAILS))
        return True
    elif response == 'b':
        state, details = select_state()
        print(state, details)
        show_image(os.getcwd() + "/images/" + state + "_flower.png")
        return True
    elif response == 'c':
        print(top_five())
        return True
    elif response == 'd':
        print(population_update())
        return True
    elif response == 'e':
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


def top_five():
    """
    Going through the dictionary looking for
    top five states with highest population
    :returns: Technically it produces two lists
    of states and populations ranked. But to avoid
    having to make a tuple in another function I call
    the plot in this one
    """
    state_populations = all_populations(STATE_DETAILS)
    state_populations.sort(reverse=True)
    five_state_names = []
    for specific_population in state_populations[0:4]:
        state_name = find_state(specific_population)
        five_state_names.append(state_name[0])
    return plot_five(five_state_names, state_populations[0:4])


def plot_five(x_values, y_values):
    """
    Bar plot of most populous state
    :x_values: A list of states for x values of graph
    :y_values: A list of ints for corresponding state pops
    :return: A bar plot based on the x_values and y_values
    """
    fig = plt.figure()
    plt_axis = fig.add_subplot(111)
    plt_axis.bar(x_values, y_values)
    plt_axis.set_title("Top 5 Most Populous States")
    plt_axis.set_ylabel("Number of People (Millions)")
    plt_axis.set_xlabel("States")
    plt_axis.set_yticks([0, 2000000, 4000000, 6000000, 8000000, 10000000,
                         12000000, 14000000, 16000000, 18000000, 20000000,
                         22000000, 24000000, 26000000, 28000000, 30000000,
                         32000000, 34000000, 36000000, 38000000])
    plt.show()


def all_options():
    """
    Shows user various options for a program
    and then prompts them with what is there selection
    :return: The characters the user types into the input
    """
    print("a. Display all U.S. States in Alphabetical Order")
    print("b. Search for a specific state and display")
    print("c. Produce a bar graph of the top 5 populated states & populations")
    print("d. Do you want to update the population?")
    print("e. Exit")
    print("\nWhat would you like to do?\n")
    return input_function("-> ")


def show_image(image_address):
    """
    :image_address: image_address for where state is located
    :return: either prints the image or it prints an error message
    """
    try:
        img = mpimg.imread(image_address)
        plt.imshow(img)
        plt.show()
    except FileNotFoundError:
        print("There is no associated image with your request.")


STATE_DETAILS = {"alabama": {"Capital": "Montgomery",
                             "Population": "4903185",
                             "Flower": "Camellia",
                             "Acronym": "AL"},
                 "alaska": {"Capital": "Anchorage",
                            "Population": "731545",
                            "Flower": "Forget-me-not",
                            "Acronym": "AK"},
                 "arizona": {"Capital": "Phoenix",
                             "Population": "7278717",
                             "Flower": "Saguaro Cactus",
                             "Acronym": "AZ"},
                 "arkansas": {"Capital": "Little Rock",
                              "Population": "3017825",
                              "Flower": "Apple Blossom",
                              "Acronym": "AR"},
                 "california": {"Capital": "Sacramento",
                                "Population": "39512223",
                                "Flower": "Golden Poppy",
                                "Acronym": "CA"},
                 "colorado": {"Capital": "Denver",
                              "Population": "578736",
                              "Flower": "Rocky Mountain Columbine",
                              "Acronym": "CO"},
                 "connecticut": {"Capital": "Hartford",
                                 "Population": "3565287",
                                 "Flower": "Mountain Laurel",
                                 "Acronym": "CT"},
                 "delaware": {"Capital": "Dover",
                              "Population": "973764",
                              "Flower": "Peach Blossom",
                              "Acronym": "DE"},
                 "florida": {"Capital": "Tallahassee",
                             "Population": "21477737",
                             "Flower": "Orange Blossom",
                             "Acronym": "FL"},
                 "georgia": {"Capital": "Atlanta",
                             "Population": "10617423",
                             "Flower": "Cherokee Rose",
                             "Acronym": "GA"},
                 "hawaii": {"Capital": "Honolulu",
                            "Population": "1415872",
                            "Flower": "Hibiscus",
                            "Acronym": "HI"},
                 "idaho": {"Capital": "Boise",
                           "Population": "1787065",
                           "Flower": "Syringa",
                           "Acronym": "ID"},
                 "illinois": {"Capital": "Springfield",
                              "Population": "12671821",
                              "Flower": "Native violet",
                              "Acronym": "IL"},
                 "indiana": {"Capital": "Indianpolis",
                             "Population": "6732219",
                             "Flower": "Peony",
                             "Acronym": "IN"},
                 "iowa": {"Capital": "Des Moines",
                          "Population": "3155070",
                          "Flower": "Wild Rose",
                          "Acronym": "IA"},
                 "kansas": {"Capital": "Topeka",
                            "Population": "2913314",
                            "Flower": "Native Sunflower",
                            "Acronym": "KS"},
                 "kentucky": {"Capital": "Frankfort",
                              "Population": "4467673",
                              "Flower": "Goldenrod",
                              "Acronym": "KY"},
                 "louisiana": {"Capital": "Baton Rouge",
                               "Population": "4648794",
                               "Flower": "Magnolia",
                               "Acronym": "LA"},
                 "maine": {"Capital": "Augusta",
                           "Population": "134412",
                           "Flower": "Pine cone & tassle",
                           "Acronym": "ME"},
                 "maryland": {"Capital": "Annapolis",
                              "Population": "6045680",
                              "Flower": "Black Eyed Susan",
                              "Acronym": "MD"},
                 "massachusetts": {"Capital": "Boston",
                                   "Population": "6949503",
                                   "Flower": "Mayflower",
                                   "Acronym": "MA"},
                 "michigan": {"Capital": "Lansing",
                              "Population": "9986857",
                              "Flower": "Apple Blossom",
                              "Acronym": "MI"},
                 "minnesota": {"Capital": "Saint Paul",
                               "Population": "5639632",
                               "Flower": "Lady Slipper",
                               "Acronym": "MN"},
                 "mississippi": {"Capital": "Jackson",
                                 "Population": "2976149",
                                 "Flower": "Magnolia",
                                 "Acronym": "MS"},
                 "missouri": {"Capital": "Jefferson City",
                              "Population": "6137428",
                              "Flower": "Hawthorn",
                              "Acronym": "MO"},
                 "montana": {"Capital": "Helena",
                             "Population": "1068778",
                             "Flower": "Bitterroot",
                             "Acronym": "MT"},
                 "nebraska": {"Capital": "Lincoln",
                              "Population": "1934408",
                              "Flower": "Goldenrod",
                              "Acronym": "NE"},
                 "nevada": {"Capital": "Carson City",
                            "Population": "3080156",
                            "Flower": "Sagebrush",
                            "Acronym": "NV"},
                 "new hampshire": {"Capital": "Concord",
                                   "Population": "1359711",
                                   "Flower": "Purple Lilac",
                                   "Acronym": "NH"},
                 "new jersey": {"Capital": "Trenton",
                                "Population": "8882190",
                                "Flower": "Purple Violet",
                                "Acronym": "NJ"},
                 "new mexico": {"Capital": "Santa Fe",
                                "Population": "2096829",
                                "Flower": "Yucca",
                                "Acronym": "NM"},
                 "new york": {"Capital": "Albany",
                              "Population": "19453561",
                              "Flower": "Rose",
                              "Acronym": "NY"},
                 "north carolina": {"Capital": "Raleigh",
                                    "Population": "10488084",
                                    "Flower": "Dogwood",
                                    "Acronym": "NC"},
                 "north dakota": {"Capital": "Bismarck",
                                  "Population": "762062",
                                  "Flower": "Wild Prairie Rose",
                                  "Acronym": "ND"},
                 "ohio": {"Capital": "Columbus",
                          "Population": "11689100",
                          "Flower": "Scarlet Carnation",
                          "Acronym": "OH"},
                 "oklahoma": {"Capital": "Oklahoma City",
                              "Population": "3956971",
                              "Flower": "Mistletoe",
                              "Acronym": "OK"},
                 "oregon": {"Capital": "Salem",
                            "Population": "4217737",
                            "Flower": "Oregon Grape",
                            "Acronym": "OR"},
                 "pennsylvania": {"Capital": "Harrisburg",
                                  "Population": "12801989",
                                  "Flower": "Mountain Laurel",
                                  "Acronym": "PA"},
                 "rhode island": {"Capital": "Providence",
                                  "Population": "1059361",
                                  "Flower": "Violet",
                                  "Acronym": "RI"},
                 "south carolina": {"Capital": "Columbia",
                                    "Population": "5148714",
                                    "Flower": "Yellow Jessamine",
                                    "Acronym": "SC"},
                 "south dakota": {"Capital": "Pierre}",
                                  "Population": "884659",
                                  "Flower": "Pasque Flower",
                                  "Acronym": "SD"},
                 "tennessee": {"Capital": "Nashville",
                               "Population": "6833174",
                               "Flower": "Purple Iris",
                               "Acronym": "TN"},
                 "texas": {"Capital": "Austin",
                           "Population": "28995881",
                           "Flower": "Texas Blue Bonnet",
                           "Acronym": "TX"},
                 "utah": {"Capital": "Salt Lake City",
                          "Population": "3205958",
                          "Flower": "Sego Lily",
                          "Acronym": "UT"},
                 "vermont": {"Capital": "Burlington",
                             "Population": "623989",
                             "Flower": "Red Clover",
                             "Acronym": "VT"},
                 "virginia": {"Capital": "Richmond",
                              "Population": "8535519",
                              "Flower": "Dogwood",
                              "Acronym": "VA"},
                 "washington": {"Capital": "Olympia",
                                "Population": "7614893",
                                "Flower": "Western Rhododendron",
                                "Acronym": "WA"},
                 "west virginia": {"Capital": "Charleston",
                                   "Population": "1792147",
                                   "Flower": "Rhododendron",
                                   "Acronym": "WV"},
                 "wisconsin": {"Capital": "Madison",
                               "Population": "5822434",
                               "Flower": "Blue Violet",
                               "Acronym": "WI"},
                 "wyoming": {"Capital": "Cheyenne",
                             "Population": "578759",
                             "Flower": "Indian paint brush",
                             "Acronym": "WY"}
                 }

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
                  "Please select one of options (a,b,c,d)"
                  " without the '.' or type (e) or EXIT to stop.\n")
    print(end_prompt())
