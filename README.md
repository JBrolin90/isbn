# ISBN Validator

A Python library for validating ISBN-10 strings using checksum verification.

## Overview

This project provides two implementations for validating ISBN-10 format:
- [`isbn.py`](isbn.py) - Standard validation with boolean returns
- [`isbn_exceptions.py`](isbn_exceptions.py) - Exception-based validation

## Features

- Cleans and normalizes ISBN strings (removes hyphens, strips whitespace)
- Validates ISBN-10 format (10 characters, 9 digits + check digit)
- Supports 'X' as the final check digit (represents 10)
- Calculates and verifies ISBN checksum using the standard algorithm

## Usage

### Basic Validation (isbn.py)

```python
from isbn import validate_isbn

# Valid ISBN examples
print(validate_isbn("0-306-40615-2"))  # True
print(validate_isbn("0306406152"))     # True
print(validate_isbn("043942089X"))     # True

# Invalid ISBN examples
print(validate_isbn("123456789"))      # False (too short)
print(validate_isbn("invalid"))        # False (invalid format)
```

### Exception-Based Validation (isbn_exceptions.py)

```python
from isbn_exceptions import validate_isbn

# Returns True for valid ISBNs, False for invalid ones
# Uses try-catch internally to handle ValueError exceptions
result = validate_isbn("0-306-40615-2")
```

## Algorithm

The ISBN-10 validation uses the following checksum algorithm:

1. Clean the input (remove hyphens, strip whitespace, convert to lowercase)
2. Validate format (exactly 10 characters, first 9 are digits, last is digit or 'x')
3. Convert to integers (treating 'x' as 10)
4. Calculate checksum: `sum(digit × position)` for positions 1-10
5. Verify checksum is divisible by 11

## Functions

### Core Functions

- [`clean_up(s)`](isbn.py) - Normalizes ISBN string format
- [`validate_content(s)`](isbn.py) - Checks basic ISBN format rules
- [`convert_to_ints(s)`](isbn.py) - Converts ISBN string to integer list
- [`caclculate_checksum(digits)`](isbn.py) - Computes ISBN checksum
- [`validate_isbn(isbn)`](isbn.py) - Main validation function

## Requirements

- Python 3.13+
- No external dependencies

## Installation

1. Clone or download the repository
2. Ensure Python 3.13+ is installed
3. Run the scripts directly or import the functions

## Running

To run interactively:

```bash
python isbn.py
# or
python isbn_exceptions.py
```

Then enter an ISBN when prompted.

## Development

This project uses:
- **Ruff** for linting and code formatting
- **MyPy** for type checking

Install development dependencies:
```bash
pip install -e ".[dev]"
```

## Note

There's a typo in the function name `caclculate_checksum` in [`isbn.py`](isbn.py) - it should be `calculate_checksum` (as correctly spelled in [`isbn_exceptions.py`](isbn_exceptions.py)).