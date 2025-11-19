"""Verifies the syntax of a provided ISBN String."""

def clean_up(s):
    return s.strip().replace("-", "").lower()

def validate_content(s):
    if len(s) != 10:
        raise ValueError("Invalid ISBN String")
    return s

def convert_to_ints(s): #Using list comprehension
    return [int(d) for d in s[:-1]] + [10 if s[-1] == "x" else int(s[-1])]

def calculate_checksum(digits):
    return sum(digit * (i + 1) for i, digit in enumerate(digits))

def validate_isbn(isbn):
    try:
        checksum = calculate_checksum(convert_to_ints(validate_content(clean_up(isbn))))
        return checksum % 11 == 0
    except ValueError:
        return False

isbn = input("ISBN String: ")
print (f"{validate_isbn(isbn)}")

