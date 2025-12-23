# Attribute Shadowing In Python

class Chai:
    temp="Hot"
    strength="Strong"
    
ginger=Chai()
print(ginger.strength) # prints Strong

ginger.temp="Mild"
ginger.cup="small"
print(f"After changing: {ginger.temp}")
print(f"Cup Size: {ginger.cup}")
print(f"Direct look into the class: {Chai.temp}")

del ginger.temp
print(ginger.temp)

del ginger.cup
print(ginger.cup)