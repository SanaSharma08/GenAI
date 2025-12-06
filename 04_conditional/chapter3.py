cup_size=input("Enter cup size (S/M/L): ").lower()
if cup_size == "s":
    print("$10")
elif cup_size == "m":
    print("$20")
elif cup_size == "l":
    print("$30")
else:
    print("Unknown Cup Size! Valid sizes: S/M/L")