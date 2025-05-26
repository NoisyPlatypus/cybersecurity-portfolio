def convert(octet: int) -> str:
    '''
    IPv4 Decimal to Binary Converter - Conversion Module
    Author: Rebecca Brown
    Course: Certificate IV in Cyber Security - Holmesglen Institute
    
    This function performs the conversion of an IPv4 address octet
    into its binary equivalent by cycling through the positional values
    of the binary system to determine the binary equivalent of the decimal
    '''

    # Initialise the list that will help build the binary number
    binary_conversion = []

    # Cycle though the positional values of the binary system to determine the
    # binary equivalent of the decimal, and adds them to the conversion list
    for positional_value in (128, 64, 32, 16, 8, 4, 2, 1):
        if octet >= positional_value:
            binary_conversion.append("1")
            octet = octet - positional_value
        else:
            binary_conversion.append("0")
    
    # Turn the list into a readable binary number, then return that value
    new_octet = "".join(binary_conversion)

    return new_octet