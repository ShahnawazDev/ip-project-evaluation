import sys
import os
os.chdir(r'D:\py\ip-project\Satwik Singh')

import importlib.util
spec = importlib.util.spec_from_file_location("metro", "metro_simulator.py")
metro = importlib.util.module_from_spec(spec)
sys.modules["metro"] = metro
spec.loader.exec_module(metro)

# Test fare function directly
print("="*60)
print("TEST: Fare calculation (direct function)")
print("="*60)
print(f"10 minutes: ₹{metro.fare(10)}")
print(f"20 minutes: ₹{metro.fare(20)}")
print(f"30 minutes: ₹{metro.fare(30)}")
print(f"45 minutes: ₹{metro.fare(45)}")
print(f"60 minutes: ₹{metro.fare(60)}")
print(f"90 minutes: ₹{metro.fare(90)}")
