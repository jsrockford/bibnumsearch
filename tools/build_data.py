# Build the bible lookup file with the correct structure 
# One time use script to build the bible_lookup.json file


import json
from data import kjv_text

print("Starting to build the bible lookup file with the correct structure...")
bible_lookup = {}

# We will use a standard for loop to handle the logic correctly
for entry in kjv_text:
    # First, validate the line to avoid errors
    if len(entry) == 3:
        book = entry[0]
        chapter_verse = entry[1]
        text = entry[2]
        
        # This is the key logic:
        # setdefault(key, []) gets the list at the key, or creates a new empty list if it's not there.
        # Then, .append() adds the new verse to that list.
        bible_lookup.setdefault(chapter_verse, []).append([book, text])

# Now, write this correctly structured dictionary to a JSON file
with open('bible_lookup.json', 'w') as json_file:
    json.dump(bible_lookup, json_file, indent=2) # No indent for a smaller, more efficient file

print(f"Successfully created bible_lookup.json with {len(bible_lookup)} unique chapter:verse keys.")