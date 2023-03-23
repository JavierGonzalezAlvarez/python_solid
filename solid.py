from abc import ABC, abstractmethod
from typing import List

class Vehicle(ABC):
    '''abstract methos for vehicle'''
    @abstractmethod
    def vehicle(self, data: List[str]) -> List[str]:
        '''pass no necessary'''

class VehicleCar(Vehicle):
    '''init'''
    def __init__(self) -> List[str]:
        pass
                 
    def vehicle(self, data: List[str]) -> List[str]:
        print("vehicle and brand: ", data[0] , " - ", data[1])
        return data

class VehicleTruck(Vehicle):
    '''init'''
    def __init__(self) -> List[str]:
        pass
                 
    def vehicle(self, data: List[str]) -> List[str]:
        print("truck and brand: ", data[0] , " - ", data[1])
        return data

class Book(ABC):
    '''init'''
    @abstractmethod
    def book(self, vehicle) -> bool:
        '''pass no necessary'''

class BookB2B(Book):
    '''init'''
    def __init__(self, company, vat, city, vehicle: Vehicle):
        self.company = company
        self.vat = vat
        self.city = city
        self.vehicle = vehicle[0:1]

    def stock(self, stock) -> int:
        '''stock, used to receive the stock'''
        self.stock = stock
        return self.stock
          
    def book(self, vehicle):
        print("vehicle to book: ", vehicle)
        if self.vehicle[0] == vehicle:
            print("company: ", self.company)
            print("vehicle: ", self.vehicle)
            print("stock: ", self.stock)
            print("vehicle car exists")
        else:             
            print("doesn't exist")
    
class BookB2P(Book):
    '''set stock'''
    stock = 5
    '''init'''
    def __init__(self, name, dni, city, vehicle: Vehicle):
        self.name = name
        self.dni = dni
        self.city = city
        self.vehicle = vehicle[0:1]

    def getstock(self) -> int:
        '''stock'''
        #self.stock = stoc
        return self.stock
    
    def book(self, vehicle):
        print("vehicle to book: ", vehicle)
        if (self.vehicle[0] == vehicle) and (self.stock != 1):
            print("name: ", self.name)
            print("truck: ", self.vehicle)
            print("stock: ", self.stock)
            print("vehicle truck exists")
        else:             
            print("doesn't exist")

vehicle1 = VehicleCar()
data_vehicle = vehicle1.vehicle(["Opel", "AQW"])

car1 = BookB2B("company", "A5672121958", "Alicante", data_vehicle)
car1.stock(1)
car1.book("Opel")

truck = VehicleTruck()
data_truck = truck.vehicle(["Man", "HTAQW"])
car2 = BookB2P("jj", "567212195Q", "Alicante", data_truck)
print("how many do we have in stock: " ,car2.getstock())
car2.book("Man")

'''
output

vehicle and brand:  Opel  -  AQW
vehicle to book:  Opel
company:  company
vehicle:  ['Opel']
stock:  1
vehicle car exists
truck and brand:  Man  -  HTAQW
how many do we have in stock:  5
vehicle to book:  Man
name:  jj
truck:  ['Man']
stock:  5
vehicle truck exists
'''