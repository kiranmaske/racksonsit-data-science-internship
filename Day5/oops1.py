class Demo:
    company = "TCS"
    def __init__(self,name):
        self.name=name
d1 = Demo("Tom")
d2 = Demo("Jerry")
print("Company Name is {}.format(d1.company)")
print("My name is {}{}".format(d1.name,d2.name))


class Test:
    company = "Capgemini"
    def __init__(self,name):
        self.name = name
    def show(self):
            print("My name is {}".format(self.name))
t1=Test("Abhi")
t2=Test("Dalavi")
t1.show()
t2.show()


class Add:
    def addition(self,a,b):
        print(a+b)
obj =Add()
obj.addition(10,20)