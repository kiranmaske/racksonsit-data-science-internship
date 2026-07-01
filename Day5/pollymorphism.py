class Birds:
    def detail(self):
        print("There are too many birds")
    def fly(self):
        print("Birds can fly")
class Sparrow(Birds):
    def fly(self):
        print("Sparrow can fly")
class Elephent(Birds):
    def fly(self):
        print("Elephent  can not fly")
b=Birds()
s=Sparrow()
e=Elephent()
b.detail()
b.fly()
s.fly()
e.fly()



