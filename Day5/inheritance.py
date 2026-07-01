class Base:
    def demo1(self):
        print("this is basic class demo1")
class Derived(Base):
    def demo2(self):
        print("This is derived class demo2")
d= Derived()
d.demo1()
d.demo2()


class Parent1:
    fname=""
    def name(self):
        print(self.name)
class Parent2:
    sname=""
    def name(self):
        print(self.sname)
class Parent3(Parent1,Parent2):
    def fullname(self):
        print("fname=",self.fname)
        print("sname=",self.sname)
# driver code
p3=Parent3()
p3.fname="John"
p3.sname="Deo"
p3.fullname()

# multi level
class Parent1:
    def __init__(self,fname):
        self.fname=fname
class  Parent2(Parent1):
    def __init__(self, sname,fname):
       self.sname=sname
       Parent1.__init__(self,fname)
class Parent3(Parent2):
    def __init__(self,lname, sname,fname):
       self.sname=sname
       Parent2.__init__(self,fname,sname)
       def display(self):
           print("fname =",self.fname)
           print("sname =",self.sname)
           print("lname =",self.lname)
           