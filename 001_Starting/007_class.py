class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print(f"Computer spec: cpu: {self.cpu}  ram: {self.ram}")





com1 = Computer('i5', 16) # Creating objects here
com2 = Computer('Ryzen 3', 8) # Creating objects here



com1.config() # Calling an object 
com2.config()
