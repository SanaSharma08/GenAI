seat_type=input("Enter seat type(Sleeper/General/AC/Luxury): ").lower()
match seat_type:
    case "sleeper":
        print("Sleeper: No AC")
    case "general":
        print("General: No reseravtion , cheapest")
    case "ac":
        print("AC: AC, Blankets, Faux Leather-Covered Beds")
    case "luxury":
        print("Luxury: Premium seats, Food")
    case _:
        print("Invalid Seat Type")