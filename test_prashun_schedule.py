import os
import sys

# Change to Prashun's directory
os.chdir("Prashun Jha")

# Test 1: Try to use code for schedule checking (same station)
print("=" * 70)
print("TEST 1: Attempting schedule check by entering same station")
print("=" * 70)
print("Inputs: Rajiv Chowk -> Rajiv Chowk at 09:18 am")
print()

# Create a test input file
test_input = """Rajiv Chowk
Rajiv Chowk
09:18
am
"""

# Run with simulated input
import subprocess
result = subprocess.run(
    [sys.executable, "metro_simulator.py"],
    input=test_input,
    capture_output=True,
    text=True
)

print("STDOUT:")
print(result.stdout)
print("\nSTDERR:")
print(result.stderr)
print("\nReturn code:", result.returncode)

if result.returncode != 0:
    print("\n❌ CODE CRASHED - Cannot use for schedule checking with same station")
else:
    print("\n✓ Code ran successfully")
    if "Next metro at" in result.stdout:
        print("✓ Shows next metro time")
    if "Journey Plan" in result.stdout:
        print("✓ Shows journey plan (even though it's same station)")
