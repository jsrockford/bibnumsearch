from data import *

def validate_input(user_input):
    if user_input.isdigit():
        if 2 <= len(user_input) <= 6:
            return True
        else:
            print("Please number 2 to 6 digits only!\n")
            return False
    else:
        print("Please enter only number 2 to 6 digits in length!\n")
        return False


# Converts user entered numbers to chapt:verse combos LIST
def convert_to_search(user_input):
    # separate digits into LIST
    num_list = []
    for i in user_input:
        num_list.append(i)

    tmp_results = []
    search_src = []
    for i in range(0, len(num_list)-1):
        tmp_list = num_list.copy()
        if i < len(num_list):
            tmp_list.insert(i + 1, ":")
            tmp_results.append(tmp_list)
            i += 1

    # code to join results into one string per entry
    a = 0
    s = ""
    while a < len(tmp_results):
        tmp_hold = tmp_results[a]
        s = "".join(tmp_hold)
        search_src.append(s)
        a += 1

    return search_src     # returns list of formatted scriptures to use in Bible search


def test_match(test_numbers, bible_lookup):
    """
    Searches for verses by doing a fast dictionary lookup.
    'test_numbers' is a list like ['1:1', '11:1'].
    'bible_lookup' is the dictionary loaded from the JSON file.
    """
    matches = []
    # Loop through the potential search keys (e.g., '1:1', '11:1', etc.)
    for num_key in test_numbers:
        
        # Use .get() to look up the key in the dictionary.
        # This will return a LIST of verses (e.g., [["Genesis", "..."], ["Exodus", "..."]])
        # or it will return None if the key is not found.
        list_of_verses = bible_lookup.get(num_key)

        # If the key was found, list_of_verses will not be None.
        if list_of_verses:
            # Now, loop through every verse that was found for that key.
            for verse_data in list_of_verses:
                book = verse_data[0]
                text = verse_data[1]

                # Build the HTML link for this specific verse and add it to our final list.
                verse_str = f'<a href="https://biblehub.com/{book.lower().replace(" ", "_")}/{num_key.replace(":", "-")}.htm" target="_blank">{book} {num_key}</a> - {text}'
                matches.append(verse_str)

    return matches
