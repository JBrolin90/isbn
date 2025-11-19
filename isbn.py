"""Verifies the syntax of a provided ISBN String."""

def clean_up(s):
    return s.strip().replace("-", "").lower()

def validate_content(s):
    if len(s) != 10 or not s[:-1].isdigit() or s[-1] not in "0123456789x":
        return False
    return s

def convert_to_ints(s): #Using list comprehension
    return [int(d) for d in s[:-1]] + [10 if s[-1] == "x" else int(s[-1])]

def caclculate_checksum(digits):
    return sum(digit * (i + 1) for i, digit in enumerate(digits))

def validate_isbn(isbn):
    cleaned_isbn = validate_content(clean_up(isbn))
    if not cleaned_isbn:
        return False
    checksum = caclculate_checksum(convert_to_ints(cleaned_isbn))
    return checksum % 11 == 0

isbn = input("ISBN String: ")
print (f"{validate_isbn(isbn)}")

