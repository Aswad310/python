class A:
    def __init__(self):
        print("Construtor of A class")

    class B:
        def __init__(self):
            print("Constructor of B class")

        def emp(self):
            print("I am in function of Class B")

a= A()
b= a.B()
b.emp()