import sys
sys.path.insert(0, r'd:\py\ip-project\Nikhil Khowal')

# Read and modify the code to avoid running main
with open(r'd:\py\ip-project\Nikhil Khowal\metro_simulator.py', 'r', encoding='utf-8') as f:
    code_lines = f.readlines()

# Find and comment out the main() call at the end
modified_code = []
for line in code_lines:
    if line.strip() == 'main()':
        modified_code.append('# ' + line)
    else:
        modified_code.append(line)

# Execute the modified code
exec(''.join(modified_code))

print("=" * 70)
print("TESTING NIKHIL KHOWAL'S METRO SIMULATOR")
print("=" * 70)

# Load data
data = load_data(r"d:\py\ip-project\Nikhil Khowal\metro_data.txt")
print(f"\n[DATA LOADED] {len(data)} station records loaded\n")

# Test 1: Same-line journey (Blue Line)
print("Test 1: Same-line journey - Dwarka to Rajiv Chowk (Blue Line)")
print("-" * 70)
result = find_route(data, "Dwarka", "Rajiv Chowk", "08:30")
print(result)
print()

# Test 2: Interchange journey (Blue to Magenta via Janakpuri West)
print("\nTest 2: Interchange journey - Dwarka to Palam (Blue to Magenta)")
print("-" * 70)
result = find_route(data, "Dwarka", "Palam", "08:30")
print(result)
print()

# Test 3: Magenta Line only
print("\nTest 3: Magenta line only - Palam to Hauz Khas")
print("-" * 70)
result = find_route(data, "Palam", "Hauz Khas", "14:00")
print(result)
print()

# Test 4: Yellow Line test
print("\nTest 4: Yellow line - Kashmere Gate to Hauz Khas")
print("-" * 70)
result = find_route(data, "Kashmere Gate", "Hauz Khas", "09:00")
print(result)
print()

# Test 5: Violet Line test  
print("\nTest 5: Violet line - Kashmere Gate to Kalkaji Mandir")
print("-" * 70)
result = find_route(data, "Kashmere Gate", "Kalkaji Mandir", "10:00")
print(result)
print()

# Test 6: Check fare calculation
print("\nTest 6: Fare Calculation Tests")
print("-" * 70)
test_stations = [1, 2, 3, 5, 8, 12, 15, 20, 25, 30]
for num in test_stations:
    print(f"{num} stations: Rs {purafare(num)}")
print()

print("=" * 70)
print("TESTING COMPLETED")
print("=" * 70)
