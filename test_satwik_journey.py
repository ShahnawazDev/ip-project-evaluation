import sys
import os

# Change to Satwik's directory
os.chdir(r'D:\py\ip-project\Satwik Singh')

# Import the code
import importlib.util
spec = importlib.util.spec_from_file_location("metro", "metro_simulator.py")
metro = importlib.util.module_from_spec(spec)
sys.modules["metro"] = metro
spec.loader.exec_module(metro)

# Test 1: Same line journey (Blue line)
print("="*60)
print("TEST 1: Same-line journey (Dwarka → Botanical Garden)")
print("="*60)
try:
    metro.planJourney("dwarka", "botanical garden", "08:22")
except Exception as e:
    print(f"ERROR: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*60)
print("TEST 2: Interchange journey (Dwarka → Botanical Garden via Magenta)")
print("="*60)
try:
    metro.planJourney("dwarka sector 21", "botanical garden", "09:00")
except Exception as e:
    print(f"ERROR: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*60)
print("TEST 3: Simple Blue Vaishali journey")
print("="*60)
try:
    metro.planJourney("dwarka sector 21", "rajiv chowk", "10:00")
except Exception as e:
    print(f"ERROR: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*60)
print("TEST 4: Blue Noida branch journey")
print("="*60)
try:
    metro.planJourney("yamuna bank", "noida city centre", "11:00")
except Exception as e:
    print(f"ERROR: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*60)
print("TEST 5: Interchange between Blue branches")
print("="*60)
try:
    metro.planJourney("dwarka sector 21", "noida electronic city", "09:00")
except Exception as e:
    print(f"ERROR: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
