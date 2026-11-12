# SCTP-AIE-Entry-Assessment
NTU SCTP AIE Technical Entry Assessment Question Answers
## Brief
This repository contains the answers to all the 3 questions in the technical entry assessment (link: https://github.com/su-ntu-sctp/sctp-aie-technical-entry-test)

## Repository Structure

| Question | Topic | File |
|---|---|---|
| Question 1 | Functions & Conditionals | `src/q1_python.py` |
| Question 2 | Arrays & Loops | `src/q2_python.py` |
| Question 3 | String Manipulation | `src/q3_python.py` |

All solutions are written in **Python 3**.

## Solution Overview

### Question 1 – Temperature Converter
- `convertTemp(value, unit)` converts between Celsius and Fahrenheit.
- Uses `if / elif / else` to choose the conversion based on the unit.
- **The unit parameter is checked before any calculation**, so an invalid unit (e.g. `"X"`) returns `-1` without the function trying to do maths on invalid input.
- Results are rounded to 2 decimal places with `round()` to avoid floating-point errors (e.g. `98.60000000000001` → `98.6`).

### Question 2 – Arrays & Loops
- `inventory` is a list that stores item names as strings.
- `addItem(itemName)` uses the `in` operator to check for duplicates before adding with `.append()`; a duplicate prints a warning instead of being added.
- `listInventory()` uses `if not inventory` to detect an empty list (an empty list is treated as `False` in Python), otherwise it prints all items.

### Question 3 – String Manipulation
- `formatName(firstName, lastName)` returns `"Lastname, Firstname"` with proper capitalisation.
- `formatInitials(firstName, lastName)` returns uppercase initials in the format `"X.Y."`.
- `.capitalize()` handles any input case (`"aLiCe"` → `"Alice"`).

## Design Notes
- Kept to the brief: e.g. a lowercase `"c"` returns `-1` in Q1 because the specification only accepts `"C"` or `"F"`.
- Known limitations (outside the brief's scope): non-numeric values with a valid unit in Q1, and empty strings in Q3, are not validated.

## AI Use Disclosure

AI tools were used for guidance and code review. All code has been written, tested and understood by me, and I am able to walk through any part of it.
