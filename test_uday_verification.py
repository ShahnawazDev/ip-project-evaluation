import subprocess
import os

# Change to Uday's directory
os.chdir(r"d:\py\ip-project\Uday Singh Tonk")

# Test 1: Schedule Logic - Check if menu works
print("=" * 60)
print("TEST 1: TESTING MENU AND SCHEDULE LOGIC")
print("=" * 60)

# Create input: option 1 (Metro_Timing), Blue line, Rajiv Chowk (R.K.Ashram Marg), time 09:18, no continue
test_input = "1\nblue\nR.K.Ashram Marg\n09:18\nn\n"

result = subprocess.run(
    [r"D:/py/ip-project/.venv/Scripts/python.exe", "2025519_metrosimulator.py"],
    input=test_input,
    capture_output=True,
    text=True,
    timeout=10
)

print("STDOUT:")
print(result.stdout)
print("\nSTDERR:")
print(result.stderr)
print("\nReturn Code:", result.returncode)

# Test 2: Journey Planner - same line
print("\n" + "=" * 60)
print("TEST 2: TESTING JOURNEY PLANNER (SAME LINE)")
print("=" * 60)

test_input2 = "2\nDwarka\nBotanical Garden\n08:22\nn\n"

result2 = subprocess.run(
    [r"D:/py/ip-project/.venv/Scripts/python.exe", "2025519_metrosimulator.py"],
    input=test_input2,
    capture_output=True,
    text=True,
    timeout=10
)

print("STDOUT:")
print(result2.stdout)
print("\nSTDERR:")
print(result2.stderr)
print("\nReturn Code:", result2.returncode)

# Test 3: Journey Planner - with interchange (Blue to Magenta)
print("\n" + "=" * 60)
print("TEST 3: TESTING JOURNEY PLANNER (INTERCHANGE)")
print("=" * 60)

test_input3 = "2\nDwarka\nHauz Khas\n08:22\nn\n"

result3 = subprocess.run(
    [r"D:/py/ip-project/.venv/Scripts/python.exe", "2025519_metrosimulator.py"],
    input=test_input3,
    capture_output=True,
    text=True,
    timeout=10
)

print("STDOUT:")
print(result3.stdout)
print("\nSTDERR:")
print(result3.stderr)
print("\nReturn Code:", result3.returncode)

print("\n" + "=" * 60)
print("ALL TESTS COMPLETED")
print("=" * 60)
