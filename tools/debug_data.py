# Debug the data.py file with the correct structure 



try:
    from data import kjv_text
except ImportError:
    print("Error: Could not find data.py. Make sure this script is in the same folder.")
    exit()

print("--- Starting scan of kjv_text in data.py ---")

error_count = 0
malformed_entries = []

# Enumerate provides both the index and the item, which is perfect for this task.
for index, entry in enumerate(kjv_text):
    # An entry is considered valid if it is a list with exactly 3 string elements.
    # We will check if it's NOT a list or if its length is NOT 3.
    if not isinstance(entry, list) or len(entry) != 3:
        error_count += 1
        # Store the index and the problematic data for a clean report at the end.
        malformed_entries.append({'index': index, 'content': entry})

print("\n--- Scan Complete ---")

# Print the final report.
if error_count == 0:
    print("✅ Success! No malformed entries were found.")
else:
    print(f"❌ Found {error_count} malformed entries. Details below:")
    for error in malformed_entries:
        # The line number in the file is usually the index + 2, because of
        # the 'kjv_text = (' line at the top of the file.
        approx_line = error['index'] + 2
        print(f"\n  - Problem Entry at Index: {error['index']} (approx. line {approx_line} in data.py)")
        print(f"    Content: {error['content']}")
        print(f"    Reason: The entry is not a list containing exactly 3 items.")

print("-" * 25)