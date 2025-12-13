import sys
import os

os.chdir(r"d:\py\ip-project\VIvaswat Kumar")

# Simulate the exact code structure
metro_line = "blue"  # User input

print(f"Testing with metro_line = '{metro_line}'")
print()

# This is the structure in the actual code:
if metro_line.lower() == "magenta":
    print("MAGENTA block executed")
elif metro_line.lower() == "blue-vaishali":
    print("BLUE-VAISHALI block executed")
    
    # ... some code in blue-vaishali block ...
    
    # This elif is INSIDE the blue-vaishali block
    elif metro_line.lower() == "blue":
        print("BLUE block executed (nested inside blue-vaishali)")
else:
    print("No matching condition")

print()
print("Result: Blue line schedule code does NOT execute")
print("The elif for blue is nested inside blue-vaishali block")
