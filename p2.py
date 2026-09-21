class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} says Meow!")
    
c1 = Cat("Meowmeow")
c1.meow()
