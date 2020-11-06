
from MenuFunctions import display_menu, capture_menu_choice
from Conversions import to_feet, to_meters, to_kilos, to_pounds, to_secs, to_hrsmins, \
    celsius_to_kelvin, kelvin_to_celsius


menu_options = {1: "Length", 2: "Mass", 3: "Temperature", 4: "Time", 0: "Quit"}
length_options = {1: "To feet and inches", 2: "To meters from feet", 0: "Quit"}
mass_options = {1: "To kgs from lbs", 2: "To lbs from kgs", 0: "Quit"}
temp_options = {1: "To C from K", 2: "To K from C", 0: "Quit"}
time_options = {1: "To secs from Mins", 2: "To Hours,Mins from secs", 0: "Quit"}


def main():
    # display main menu and capture user choice
    display_menu(menu_options)
    conversion_type = -1
    while conversion_type == -1:
        conversion_type = capture_menu_choice(menu_options)
    if conversion_type == "Length":
        sub_menu = length_options
    if conversion_type == "Mass":
        sub_menu = mass_options
    if conversion_type == "Temperature":
        sub_menu = temp_options
    if conversion_type == "Time":
        sub_menu = time_options

    # display specific sub-menu and capture user choice
    display_menu(sub_menu)
    function_type = -1
    while function_type == -1:
        function_type = capture_menu_choice(sub_menu)
    value = input("Input original value: ")
    function_library = {"To feet and inches": to_feet(float(value)),
                        "To meters from feet": to_meters(float(value)),
                        "To kgs from lbs": to_kilos(float(value)),
                        "To lbs from kgs": to_pounds(float(value)),
                        "To K from C": celsius_to_kelvin(float(value)),
                        "To C from K": kelvin_to_celsius(float(value)),
                        "To secs from Mins": to_secs(float(value)),
                        "To Hours,Mins from secs": to_hrsmins(float(value))}

    print(function_library[function_type])

if __name__ == "__main__":
    main()


