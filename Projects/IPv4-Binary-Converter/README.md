# IPv4 Decimal to Binary Converter

A Python command-line tool that converts IPv4 addresses from decimal notation to binary format, developed as part of my cybersecurity studies at Holmesglen Institute.

## 🎯 Project Overview

This tool demonstrates understanding of:
- IPv4 addressing and subnetting concepts
- Binary number systems
- Input validation and error handling
- User-friendly CLI design
- Modular programming principles
- Security-conscious development practices

## ✨ Features

- ✅ Converts any valid IPv4 address to binary format
- ✅ Comprehensive input validation
- ✅ User-friendly command-line interface
- ✅ Continuous conversion capability
- ✅ Multiple exit options (quit/exit commands)
- ✅ Clear error messages for invalid inputs
- ✅ Modular code architecture

## 🚀 Usage

```bash
python main.py
```

### Example Session:
```
Welcome to the IPv4 Decimal to Binary Address Converter

This program can convert a decimal IPv4 address into its binary equivalent
>> You can exit at any time by typing "quit" or "exit" <<

Do you want to convert an IPv4 address to binary? Yes

Please enter the IPv4 address you'd like to convert: 192.168.1.1

The IPv4 decimal address of 192.168.1.1 is equivalent to 
11000000.10101000.00000001.00000001 in binary.

Do you want to convert another address? (Y/N): n

Thanks for using the converter. I hope you found it useful!
❤️ Have a nice day ❤️
```

## 📸 Screenshots

### Successful Conversion
![Successful IPv4 conversion](./screenshots/successful_conversion.png)
*Converting common private network addresses to their binary equivalents*

### Input Validation
![Invalid input handling](./screenshots/invalid_input_handling.png)
*Robust error handling for invalid IPv4 formats - the program catches non-numeric values and continues gracefully*

### User-Friendly Exit Options
![Quit functionality](./screenshots/quit_functionality.png)
*Users can exit at any time by typing 'quit' or 'exit' - the program responds with a friendly farewell*

### Program Flow Control
![Program flow demonstration](./screenshots/program_flow.png)
*Clean start/stop flow - users can choose not to begin conversion or exit after completing conversions*

## 🔄 Program Logic

![IPv4 Converter Flowchart](./documentation/program_flowchart.png)
*Program flow diagram showing input validation, conversion logic, and user interaction loops*

## 📋 Input Validation

The program validates:
- Correct number of octets (must be 4)
- Valid separators (periods)
- Numeric values only
- Range validation (0-255 for each octet)

Invalid inputs receive helpful error messages:
- "Invalid IPv4 address" with prompt to try again
- Specific guidance on valid format
- Graceful error recovery

## 🔍 Code Architecture

### Modular Design
The application follows clean code principles with separated concerns:

```
main.py          # Program entry point and user interaction
├── validation.py # Input validation logic
└── conversion.py # Binary conversion algorithm
```

### Project Structure
```
IPv4-Binary-Converter/
├── README.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── conversion.py
│   └── validation.py
├── documentation/
│   ├── pseudocode.txt
│   ├── user_documentation.pdf
│   └── program_flowchart.png
├── screenshots/
│   ├── successful_conversion.png
│   ├── invalid_input_handling.png
│   ├── quit_functionality.png
│   └── program_flow.png
├── requirements.txt
└── .gitignore
```

### Key Security Features

1. **Input Validation** (`validation.py`)
   - Prevents injection attacks through strict input checking
   - Validates format, data type, and range
   - Returns clear error messages without exposing internals

2. **Safe Type Conversion**
   - Explicit string to integer conversion with error handling
   - No use of `eval()` or other unsafe methods
   - Bounded input ranges (0-255)

3. **User Input Sanitization**
   - `.strip()` to remove whitespace
   - `.lower()` for case-insensitive commands
   - Whitelist approach for valid commands

### Algorithm Efficiency
- O(1) time complexity for each octet conversion
- No recursive calls preventing stack overflow
- Memory efficient with list comprehensions

### Code Quality
- Comprehensive docstrings for all functions
- Modular design with single responsibility principle
- PEP 8 compliant formatting
- Meaningful variable names
- Professional file headers with attribution

## 🏗️ Technical Implementation

### Algorithm
1. Parse input string into four octets
2. Validate each octet (numeric, 0-255 range)
3. Convert each decimal octet to 8-bit binary
4. Format and display the result

### Key Functions
- `validate_input()`: Ensures input meets IPv4 standards
- `convert()`: Converts decimal to 8-bit binary string
- `run_program()`: Main program loop with error handling

## 📚 Documentation

- [Pseudocode](./documentation/pseudocode.txt) - Detailed algorithm design
- [User Documentation](./documentation/user_documentation.pdf) - End-user guide
- [Program Flowchart](./documentation/program_flowchart.png) - Visual program flow

## 🔧 Requirements

- Python 3.6+
- No external dependencies (uses standard library only)

## 🎓 Learning Outcomes

This project helped me understand:
- How IPv4 addresses work at the binary level
- The importance of input validation in security applications
- Creating user-friendly command-line interfaces
- Writing modular, maintainable code
- Following programming best practices
- The value of comprehensive documentation

## 🔮 Future Enhancements

- [ ] Add IPv6 support
- [ ] Include subnet mask calculations
- [ ] Create a GUI version
- [ ] Add reverse conversion (binary to decimal)
- [ ] Export results to file
- [ ] Add CIDR notation support

## 🙏 Acknowledgments

Developed as part of Certificate IV in Cyber Security at Holmesglen Institute. Special thanks to my instructors for teaching the networking fundamentals that made this project possible.

## 📝 License

This project is part of my educational portfolio and is available for reference and learning purposes.

---
*Developed by Rebecca Brown - Cybersecurity Student*