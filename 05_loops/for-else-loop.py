staff = [
    ("Alice", 22),
    ("Benjamin", 31),
    ("Charlotte", 19),
    ("David", 32),
    ("Emma", 18),
    ("Frank", 28),
    ("Grace", 26),
    ("Henry", 21),
    ("Isabella", 17),
    ("Jack", 30),
    ("Katherine", 24),
    ("Liam", 16),
]

for name, age in staff:
    if age < 21:
        print(f"{name} is underage at {age} years old.")
        break
else:
    print("All staff members are of legal age.")