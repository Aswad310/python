class Student:
    def sum(self, *a):
        ans=0
        for i in a:
            ans= ans+i
        print(ans)

std= Student()
std.sum(1, 2, 4)
std.sum(1)
std.sum(10, 20)