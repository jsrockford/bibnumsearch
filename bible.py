# Bible Number Lookup program to be renamed better later
# Program takes 2-6 digit user number input then returns "Book Chapter:Verse - Text" formatted results
# This script is modified 'main.py' for Flask use on website to accept one input then return answer
from functions import *


def scriptures(my_number):

    # Converts user input to concatenated numbers in verse form, saves in list
    src_numbers = convert_to_search(my_number)

    # Search KJV for matching verses, save in 'answer'
    answer = test_match(src_numbers)

    # for scripture in answer:
    #     print(f"{scripture[0]} {scripture[1]} - {scripture[2]}")

    print(answer)

    return answer

