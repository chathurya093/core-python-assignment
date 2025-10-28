def calculate_fare(distance, base_fare=50, rate_per_km=10):
    return base_fare + (distance * rate_per_km)
n = int(input("Enter number of trips: "))
trips = []
for i in range(n):
    distance = int(input(f"Enter distance for trip {i+1} (in km): "))
    trips.append(distance)

total_fare = 0
for i, distance in enumerate(trips, start=1):
    fare = calculate_fare(distance)
    print(f"Trip {i}: ${fare}")
    total_fare += fare

print(f"\nTotal Fare: ${total_fare}")
