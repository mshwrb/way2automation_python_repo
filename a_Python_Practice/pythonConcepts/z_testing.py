class A():
    def __init__(self, alphabet):
        self.a = alphabet
        print(self.a)

    def A(self):
        print(f"inside A function {self.a}")


class B():
    def __init__(self, alphabet):
        self.b = alphabet
        print(self.b)

    def B(self):
        print(f"inside B function {self.b}")


class C(A, B):
    def __init__(self, alphabet):
        self.c = alphabet
        print("inside C constructor")
        A.__init__(self, alphabet)
        B.__init__(self, alphabet)

    def C(self):
        print(f"inside C function {self.c}")


obj = C("inside C")
