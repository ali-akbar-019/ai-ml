# MRO - Method Resolution Order
# order matter krta ha yaha
# jon sa pehle pass hoga us ka method run ho ga

class A:
    def test(self):
        print("A")


class B:
    def test(self):
        print("B")

# order matter krta ha iders
class C(B,A):   
    pass

obj = C()
obj.test()