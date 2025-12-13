import subprocess
import sys

# Test journey planner
test_input = "2\nDwarka\nBotanical Garden\n08:22\n"
result = subprocess.run(
    [r"D:/py/ip-project/.venv/Scripts/python.exe", "metro_simulation.py"],
    input=test_input,
    capture_output=True,
    text=True,
    cwd=r"d:\py\ip-project\Parag Prashun"
)

print("=== STDOUT ===")
print(result.stdout)
print("\n=== STDERR ===")
print(result.stderr)
print("\n=== Return Code ===")
print(result.returncode)
