import sys
import os
os.chdir(r'D:\py\ip-project\Satwik Singh')

import importlib.util
spec = importlib.util.spec_from_file_location("metro", "metro_simulator.py")
metro = importlib.util.module_from_spec(spec)
sys.modules["metro"] = metro
spec.loader.exec_module(metro)

# Temporarily fix the termm dictionary
metro.termm["orange"] = ["dwarka sector 21", "new ashok nagar"]  # Adding second terminal

print("="*60)
print("TEST: After fixing Orange line terminal bug")
print("="*60)

print("\nTEST 1: Simple Blue Vaishali journey")
try:
    metro.planJourney("dwarka sector 21", "rajiv chowk", "10:00")
    print("✓ SUCCESS")
except Exception as e:
    print(f"✗ FAILED: {e}")

print("\n" + "="*60)
print("TEST 2: Blue to Magenta interchange")
try:
    metro.planJourney("dwarka sector 21", "botanical garden", "09:00")
    print("✓ SUCCESS")
except Exception as e:
    print(f"✗ FAILED: {e}")

print("\n" + "="*60)
print("TEST 3: Blue Noida branch")
try:
    metro.planJourney("yamuna bank", "noida city centre", "11:00")
    print("✓ SUCCESS")
except Exception as e:
    print(f"✗ FAILED: {e}")
