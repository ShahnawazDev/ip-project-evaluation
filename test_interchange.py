import os
os.chdir('manan')
exec(open('metro_simulator.py').read().replace('if __name__ == "__main__":', 'if False:'))

# Test interchange journey specifically
data = loadmetro("metro_data.txt")
print("\n=== DETAILED INTERCHANGE TEST ===")
result = planjourney("Dwarka", "Botanical Garden", "08:22", data)
print("Result dictionary:", result)
print()
if "interchange" in result:
    print("✓ Interchange detected correctly")
else:
    print("✗ Interchange not detected in result")
