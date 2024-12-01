class Animals:
  def __init__(self, name):
    self.name = name
  def eat(self):
    print(f"{self.name}(Animals): is eating...")
  def sleep(self):
    print(f"{self.name}(Animals): is sleeping...")

class Cat(Animals):
  def meow(self):
    print(f"{self.name}(Cat): is is meowing...")

class Dog(Animals):
  def bark(self):
    print(f"{self.name}(Dog): is barking...")
  def eat(self):
    print(f"{self.name}(Dog): eating...")
  def sleep(self):
    print(f"{self.name}(Dog): sleeping...")

# using defult function body
cat = Cat("mekky")
cat.meow()
cat.eat()
cat.sleep()

# using custom function body
dog = Dog("r3d")
dog.bark()
dog.eat()
dog.sleep()