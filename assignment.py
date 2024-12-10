class Phone:
    def __init__(self, name, phoneVersion, memorySize, batteryCapacity, network, brand):
        self.name = name
        self.phoneVersion = phoneVersion
        self.memory = memorySize
        self.battery = batteryCapacity
        self.network = network
        self.brand = brand

    def version (self):
        print(f"The android version is  : {self.phoneVersion}")

myPhone = Phone("Tecno Spark5", 10, "64gb", 5000, "4G", "Tecno")
myPhone.version()
print(myPhone.network)

class My_ios(Phone):
    def __init__(self, name, phoneVersion, memorySize, batteryCapacity, network, brand):
        super().__init__(name, phoneVersion, memorySize, batteryCapacity, network, brand)

    def version(self):
        print(f"The ios version is  : {self.phoneVersion}")

class Animal:
    def __init__(self):
        pass


    def move(self):
        print("Move")

class Bird(Animal):
    def __init__(self):
        super().__init__()

    def move(self):
        print("Fly")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def move(self):
        print("Swim")

class Snake(Animal):
    def __init__(self):
        super().__init__()

    def move(self):
        print("Crawl")

mySecondPhone = My_ios("iphone 16", "latest ios", "128gb", 5000, "5G", "Apple")
mySecondPhone.version()
animal = Animal()
animal.move()

bird = Bird()
bird.move()

fish = Fish()
fish.move()

snake = Snake()
snake.move()