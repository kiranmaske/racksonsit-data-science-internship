#  Itvbwill alows programers to modify function behaviour

def show(func):
    def inner():
        print("CAtching Decorators")
        func()
    return inner()

def ordinary():
    print("Yes I Am Ordinary")
    
dfunc = show(ordinary)
dfunc()