# You want to simulate tea heating.
# It starts at 40C and boils at 100C.
# Task:
# • Use a white loop.
# • Increase temperature by 15 until it reaches or exceeds 100.
# • Print each temperature step.

temperature = 40
while temperature <= 100:
    print(f"Current temperature: {temperature}C")
    temperature += 15