import sys
import os
os.chdir(r'D:\py\ip-project\Satwik Singh')

import importlib.util
spec = importlib.util.spec_from_file_location("metro", "metro_simulator.py")
metro = importlib.util.module_from_spec(spec)
sys.modules["metro"] = metro
spec.loader.exec_module(metro)

# Fix the Orange line terminal bug
metro.termm["orange"] = ["dwarka sector 21", "new ashok nagar"]

print("="*60)
print("TEST: Fare Calculator Menu (after fixing Orange line)")
print("="*60)

# Simulate fare menu with inputs
import io
from unittest.mock import patch

# Test 1: Simple Blue journey
print("\nTest 1: Dwarka Sector 21 to Rajiv Chowk")
with patch('builtins.input', side_effect=["dwarka sector 21", "rajiv chowk", "10:00"]):
    try:
        metro.faremenu()
    except StopIteration:
        pass

# Test 2: Blue to Magenta
print("\n" + "="*60)
print("Test 2: Dwarka to Botanical Garden")
with patch('builtins.input', side_effect=["dwarka", "botanical garden", "08:00"]):
    try:
        metro.faremenu()
    except StopIteration:
        pass
