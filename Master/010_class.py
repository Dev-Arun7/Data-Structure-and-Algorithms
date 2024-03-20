#Types of variables
#Instance variable will change according to the object where as class varible stays as it is.

class Car:

    #class variable
    wheels = 4

    def __init__(self):
        #Instance varible
        self.mil = 10
        self.brand = "BMW"
 
c1 = Car()
c2 = Car()

c1.mil = 8
Car.wheels = 6

print(c1.brand, c1.mil, c1.wheels)
print(c2.brand, c2.mil, c2.wheels) 