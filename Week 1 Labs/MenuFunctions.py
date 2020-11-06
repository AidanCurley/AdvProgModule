import sys


def display_menu(menu):
    for option in menu:
        print(f"{option}: {menu[option]}")


def capture_menu_choice(menu):
    # ask for input
    chosen_option = input("Please choose: ")
    if chosen_option == "0":
        sys.exit("ByeBye")
    try:
        choice = menu[int(chosen_option)]
    except:
        return -1

    return choice
