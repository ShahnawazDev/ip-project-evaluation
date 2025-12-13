import sys
import os
os.chdir(r'D:\py\ip-project\Satwik Singh')

import importlib.util
spec = importlib.util.spec_from_file_location("metro", "metro_simulator.py")
metro = importlib.util.module_from_spec(spec)
sys.modules["metro"] = metro
spec.loader.exec_module(metro)

print("="*60)
print("TEST: Schedule Logic for Rajiv Chowk at 09:18")
print("="*60)
metro.nxtmet(None, "rajiv chowk", "09:18")

print("\n" + "="*60)
print("TEST: Schedule Logic for Yamuna Bank at 10:00 (both branches)")
print("="*60)
metro.nxtmet(None, "yamuna bank", "10:00")

print("\n" + "="*60)
print("TEST: Schedule Logic for Janakpuri West at 08:00 (interchange)")
print("="*60)
metro.nxtmet(None, "janakpuri west", "08:00")
