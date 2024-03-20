# How to use class and object

class Computer:
    def __init__(self, cpu, ram):
        self.c = cpu
        self.r = ram

    def config(self):
        print(f"Spec is: {self.c} and {self.r}")


com1 = Computer('i5', 16)
com2 = Computer('Ryzen 3', 8)


com1.config()
com2.config()




 