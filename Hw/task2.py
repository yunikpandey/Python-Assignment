from statistics import mean
print("Swallow Speed Analysis: Version 1.0 ")
km = []
while True:
    read = input("Enter next reading: ")
    if read == "":
        break
    elif read[0] == "U":
        km.append(float(read[1:])*1.61)
        print("Reading saved")
    elif read[0] == "E":
        km.append(float(read[1:]))
        print("Reading saved")

if len(km) == 0:
    print("No reading entered. No thing to do.")
else:
    maximum_km = max(km)
    maximum_miles = maximum_km/1.61
    minimum_km = min(km)
    minimum_miles = minimum_km/1.61
    average_km = mean(km)
    average_miles = average_km/1.61
    print("\nReading Summary\n")
    print(len(km)," Readings Analysed\n")
    print(f"Maximum speed {maximum_miles:.2f} MPH, {maximum_km:.2f} KPH")
    print(f"Minimum speed {minimum_miles:.2f} MPH, {minimum_km:.2f} KPH")
    print(f"Average speed {average_miles:.2f} MPH, {average_km:.2f} KPH")
