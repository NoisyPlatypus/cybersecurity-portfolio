'''
IPv4 Decimal to Binary Converter - Main Module
Author: Rebecca Brown
Course: Certificate IV in Cyber Security - Holmesglen Institute
Version: 1.1.0
Last Updated: May 2025

This module provides the main program logic for converting IPv4 addresses
from decimal to binary format with comprehensive input validation.

Note: Version 1.1.0 fixes input validation bug found post-submission
'''

# Import the custom modules to check for valid input and conversion
import validation, conversion

# Create the function to start the script over in case the user doesn't 
# supply a valid IPv4 address.
def start_over() -> tuple:
    '''
    This function runs the beginning of the script again in case the user
    provided an invalid IPv4 address, prompting them for an IPv4 address,
    splitting it into workable segments, and running it through the
    validation checking module.
    '''
    ip_address = input(
                       "\nPlease enter the IPv4 address you'd "
                       "like to convert: "
                      )
    string_octets = ip_address.split(".")
    valid = validation.check(string_octets)
    return valid, ip_address, string_octets

# Create a function to set the valid options to continue, and checks the
# user input agaist them
def get_yes_no_response(prompt: str) -> str:
    '''
    This function gets a validated yes/no response from the user.
    It accepts y, n, yes, no, quit, or exit as valid responses.
    '''
    valid_responses = ["y", "n", "yes", "no", "quit", "exit"]
    while True:
        response = input(prompt).strip().lower()
        if response in valid_responses:
            return response
        else:
            print("\nPlease answer with a Yes, No, Y, or N\n")

# Create a function that farewells the user and quits the program
# This will be called if the user types "quit" or "exit"
def exit_program() -> None:
    print(farewell_message)
    exit()

# Create the function that performs the conversion so that it can be reused
def run_program(ip_address: str = None, decimal_octets: list = None) -> None:
    '''
    This function is the main body of the code. It obtains an input from the
    user, checks it's validity, performs the conversion and returns the result
    '''
    # If ip_address is not provided, ask the user for the IP address
    if ip_address is None:
        ip_address = input(
                           "\nPlease enter the IPv4 address you'd like "
                           "to convert: "
                          ).strip().lower()
        # Check for the user prompting to exit the program and run exit
        # function if needed   
        if ip_address in ["quit", "exit"]:
            exit_program()
        else:
            decimal_octets = ip_address.split(".")

    # Launch the validation module to check the input is a valid IPv4 address
    # and store the result in a variable to determine next steps.
    valid = validation.check(decimal_octets)

    # Check the results of the validation and either prompt the user for a new
    # IPv4 address, or launch the conversion module by looping until a valid 
    # IP address is entered
    while not valid:
        print(f"{ip_address} is not a valid IPv4 address.")
        # Reset the variables and rerun the start of the script
        valid, ip_address, string_octets = start_over()
        decimal_octets = string_octets
        
    # Convert octets from string to integers
    decimal_octets = [int(each) for each in decimal_octets]

    # For each of the octets in the IP address, run them through the conversion 
    # module and store them in a new list
    converted_octets = [conversion.convert(part) for part in decimal_octets]

    # Join all of the binary octets together to get the binary IPv4 address
    converted_address = ".".join(converted_octets)

    print(
          f"\nThe IPv4 decimal address of {ip_address} is equivalent to"
          f" {converted_address} in binary."
         )

# Set a farewell message to be called if the program is going to end
farewell_message = (
                   "\nThanks for using the converter. I hope you found it useful!"
                   "\n\n\u2764  Have a nice day \u2764\n"
                   )
# Introduce the program and prompt the user to start the script
print("\n\033[4mWelcome to the IPv4 Decimal to Binary Address Converter\033[0m\n\n"
      "This program can convert a decimal IPv4 address into its binary "
      "equivalent\n>> You can exit at any time by typing \"quit\" or \"exit\" <<\n"
     )

# Prompt the user to either start or quit the program
begin = get_yes_no_response("Do you want to convert an IPv4 address to binary?  ")

# Run the conversion function as many times as the user has numbers
while begin.lower() == "y" or begin.lower() == "yes":
    run_program()
    # Ask if the user has another number to convert to either keep the script
    # running or exit the converter
    begin = get_yes_no_response("\nDo you want to convert another address? (Y/N):  ")

# Farewell the user before exiting the program (because manners are important)
print(farewell_message)