import os
os.chdir('manan')
exec(open('metro_simulator.py').read().replace('if __name__ == "__main__":', 'if False:'))

data = loadmetro("metro_data.txt")

print("=== TEST: Blue to Magenta Interchange ===")
# Dwarka (Blue only) to IIT Delhi (Magenta only)
result = planjourney("Dwarka", "IIT Delhi", "08:22", data)
printjourney(result)

print("\n=== TEST: Magenta to Blue Interchange ===")
# Hauz Khas (Magenta) to Rajiv Chowk (Blue)
result = planjourney("Hauz Khas", "Rajiv Chowk", "09:00", data)
printjourney(result)
