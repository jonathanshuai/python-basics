class A():
    def __init__(self):
        self.common = "Apple"
        self.key = "Pie"

    def print_common_and_key(self):
        print(f"A {self.common} {self.key}")


class B():
    def __init__(self):
        self.common = "Banana"
        self.key = "Ice Cream"

    def print_common_and_key(self):
        super(B, self).print_common_and_key()
        print(f"B {self.common} {self.key}")


class C(A, B):
    def __init__(self):
        super(C, self).__init__()

        self.common = "Coffee"
        self.key = "Cake"

    def print_common_and_key(self):
        print(f"C {self.common} {self.key}")
