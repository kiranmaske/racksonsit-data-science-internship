class Base:
    def __init__(self):
        self.a = "Welcome"
        self.b = "To Data Science"
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling base class private members")
        print(self.b)
b=Base()
print(b.a)
d=Derived()



from abc import ABC, abstractmethod
class Animal(ABC):
    def action(self):
        pass
class Person(Animal):
    def action(self):
        print("Person say he can run and work")
class Snake(Animal):
    def action(self):
        print("Snake say he can Crawling")
class Dog(Animal):
    def action(self):
        print("Dog say he can run ")
class Lion(Animal):
    def action(self):
        print("Lion says he is Roaring ")
p = Person()
p.action()
s = Snake()
s.action()
d = Dog()
d.action()
l = Lion()
l.action()


from abc import ABC,abstractmethod
class Polygon(ABC):
    @abstractmethod
    def sides(self):
        pass
class Tringle(Polygon):
      def sides(self):
          print("3 sides")
class Pentagon(Polygon):
      def sides(self):
          print("5 sides")
t = Tringle()
t.sides()
p = Pentagon()
p.sides()

        