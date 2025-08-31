# Bible Number Lookup program to be renamed better later
# Program takes 2-6 digit user number input then returns "Book Chapter:Verse - Text" formatted results
# This script is modified 'main.py' for Flask use on website to accept one input then return answer
# bible.py

import json
from functions import convert_to_search, test_match

# --- DATA LOADING (This happens once when the app starts) ---
# We're loading the efficient JSON data into a dictionary called 'bible_lookup'.
print("Loading Bible lookup data from bible_lookup.json...")
try:
    # Open the file and use json.load() to create the dictionary
    with open('bible_lookup.json', 'r') as f:
        bible_lookup = json.load(f)
    print("Bible data loaded successfully.")
except FileNotFoundError:
    print("\nFATAL ERROR: 'bible_lookup.json' was not found!")
    print("Please run 'build_data.py' to create it before starting the app.\n")
    bible_lookup = {} # Define as empty to prevent a crash
# --- END DATA LOADING ---


def scriptures(my_number):
    """
    This is the main function called by your web server.
    """
    # 1. Convert the user's number (e.g., "316") into potential search keys (e.g., ["3:16"])
    src_numbers = convert_to_search(my_number)

    # 2. Pass those keys AND the loaded bible_lookup data to the search function
    answer = test_match(src_numbers, bible_lookup)

    return answer

