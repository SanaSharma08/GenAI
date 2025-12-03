sugar=set()
print(f"Initial set: {sugar}")
print(f"Initial set id: {id(sugar)}") #Initial set id: 1578683859680
sugar.add("cinnamon")
sugar.add("ginger")
sugar.add("cloves")
print(f"Mutated set sugar: {sugar}")
print(f"Mutated set sugar id: {id(sugar)}") #Mutated set sugar id: 1578683859680
#Sets are mutable : id same, value can be changed and reference also remains same(variables points to same object, and the value of the object can be mutated in the memory)