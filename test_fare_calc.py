# Test fare calculator logic
def calculate_fare(mins):
    if mins<=10: 
        return 11
    elif mins<=25: 
        return 21
    elif mins<=45: 
        return 32
    elif mins<=65: 
        return 43
    elif mins<=90: 
        return 54
    else: 
        return 64

# Test various travel times
test_times = [5, 10, 15, 25, 30, 45, 50, 65, 70, 90, 100]

print("Fare Calculator Test:")
print("=" * 40)
for time in test_times:
    fare = calculate_fare(time)
    print(f"{time} minutes: ₹{fare}")
