class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
        print(self.m1, self.m2)

    # method overload option in python
    def mo(self,a=None, b=None, c=None):
        s =0

        if a!= None and b != None and c != None:

            print (type(a))
            s = a + b + c
            return s
        elif a is not None and b is not None:
            s = a + b
            return s
        else:
            s= a
            return s


s1 = student(23, 43)
print(s1.mo(2))
