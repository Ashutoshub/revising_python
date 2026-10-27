class Car:# class definition
    def __init__(self, brand, model): # constructor method
        self.__brand = brand #__ for encapsulation.
        self.model = model
    def get_brand(self): #get the encapsulated data __ is for private making it.
        return self.__brand
    def full_name(self): # method to return the full name of the car
        return f"{self.__brand} {self.model}"
    def fuel_type(self): # method to return the fuel type of the car
        return "Gasoline"
    @staticmethod #can not be accesed by objects of the class 
    # but can be accessed by the class itself. It does not require self parameter.
    def car_info(): # also inside self not used static method to return general information about cars
        return "Cars are vehicles that are used for transportation."
class ElectricCar(Car): # Inheritance
    def __init__(self, brand, model, battery_size): # constructor methodElectricCar
        super().__init__(brand, model)
        self.battery_size = battery_size
    def full_name(self):
        return f"{self.brand} {self.model} with a {self.battery_size}-kWh battery"
    def fuel_type(self): #polymorphism
        return "Electric"
my_car = Car("Toyota", "Corolla")
# print(my_car.get_brand())  # Output: Toyota
# print(my_car.model)  # Output: Corolla
# print(my_car.full_name())  # Output: Toyota Corolla
print(my_car.fuel_type())  # Output: Gasoline
my_electric_car = ElectricCar("Tesla", "Model 3", 75)
# print(my_electric_car.full_name())  # Output: Tesla Model 3 with a 75-kWh battery
print(my_electric_car.fuel_type())  # Output: Electric
print(Car.car_info())  # Output: Cars are vehicles that are used for transportation.