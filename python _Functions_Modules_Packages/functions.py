def f1():
    def f2():
        print("This is return of f2")
    return f2
c= f1()
c()