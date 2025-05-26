def check(segment: list) -> bool:
    '''
    IPv4 Decimal to Binary Converter - Validation Module
    Author: Rebecca Brown
    Course: Certificate IV in Cyber Security - Holmesglen Institute

    This module provides input validation to ensure security and data integrity.
    '''
    while True:
        # Checks that there are the right number of sections
        if len(segment) != 4:
            valid = False
            break
        # Checks that all sections are positive numbers only - this will
        # also check if symbols other than "." were used in the address
        elif all(item.isdecimal() for item in segment) is False:
            valid = False
            break
        #Checks that all sections are less than 256
        elif all(int(item) < 256 for item in segment) is False:
            valid = False
            break
        else:
            valid = True
            break
    return valid