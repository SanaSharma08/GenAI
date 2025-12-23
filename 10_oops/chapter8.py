# Method Resolution Order

class A:
    label="A: Ginger"
class B(A):
    label="B: Rose"
class C(A):
    label="C: Tulsi"
    
class D(C,B): # Here the order of inheritence Matters
    pass

cup=D()
print(D.__mro__)
print(cup.label)

class F(B,C):
    pass
cup2=F()
print(cup2.label) # would give label from B since we reverse the inheritense order in comparison to D