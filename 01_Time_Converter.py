minutes = int(input("Enter minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print("Output:", hours, "hrs", remaining_minutes, "minutes")