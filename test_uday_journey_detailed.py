import subprocess
import os

os.chdir(r"d:\py\ip-project\Uday Singh Tonk")

# More comprehensive journey planner tests
tests = [
    ("Same-line Blue", "2\nDwarka Sector - 21\nRajendra Place\n09:00\nn\n"),
    ("Same-line Magenta", "2\nBotanical Garden\nHauz Khas\n09:00\nn\n"),
    ("Blue to Magenta via Botanical Garden", "2\nNoida Electronic City\nHauz Khas\n08:00\nn\n"),
    ("Blue to Magenta via Janakpuri", "2\nDwarka Sec - 11\nPalam\n10:00\nn\n"),
    ("Magenta to Blue", "2\nHauz Khas\nKarol Bagh\n09:00\nn\n"),
]

for test_name, test_input in tests:
    print("\n" + "=" * 80)
    print(f"TEST: {test_name}")
    print("=" * 80)
    
    result = subprocess.run(
        [r"D:/py/ip-project/.venv/Scripts/python.exe", "2025519_metrosimulator.py"],
        input=test_input,
        capture_output=True,
        text=True,
        timeout=10
    )
    
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    if result.returncode != 0:
        print("ERROR: Return code", result.returncode)
