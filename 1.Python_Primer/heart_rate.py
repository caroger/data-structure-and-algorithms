age = int(input("Please Enter Your Age in Years: "))
max_heart_rate = 206.9 - (0.67 * age)
target = 0.65 * max_heart_rate

print(f"Your target fat-burning heart rate is {target:0.2f}")