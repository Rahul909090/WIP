# -*- coding: utf-8 -*-
"""
Created on Wed May  1 13:58:19 2024

def __init__(self, ID, X, Y):
    constructor

def containerInPort(self, contObj):
    takes as an input a container object and returns true if it exists in containers list of Container objects

def removeCurrentShips(self, shipObj):
    takes as an input a ship object and removes the ship if exists from currentShips list of Ship objects

def removeContainer(self, contObj):
    takes as an input a a container object and removes the ship if exists from containers list of Container objects

def incomingShip(self, shipObj):
    takes as an input a Ship object and returns nothing. incomingShip adds the ship to the currentShips
    list if it doesn't exit in currentShips

def outgoingShip(self, shipObj):
    takes as an input a Ship object and returns nothing. outgoingShip adds the ship to the shipsHistory 
    list if it doesn't exit in shipsHistory

def getDistance(self, portObj):
   takes as an input a Port object and returns the distance between the object itself and another Port
   
class Container:
    def __init__(self, ID, weight):
        constructor
        
    #setter and getters for ID and weight

class BasicContainer(Container):
    def __init__(self, ID, weight):
        the constructor calls parents constructor
    
    def consumption(self):
        Override consumption method. The method takes no input and returns 2.50 * weight

class HeavyContainer(Container):
    def __init__(self, ID, weight):
        the constructor calls parents constructor
        
    def consumption(self):
        Override consumption method. The method takes no input and returns 3.00 * weight

class LiquidContainer(HeavyContainer):
    def __init__(self, ID, weight):
        the constructor calls parents constructor
    
    def consumption(self):
        Override consumption method. The method takes no input and returns 4.00 * weight

class RefrigeratedContainer(HeavyContainer):
    def __init__(self, ID, weight):
        the constructor calls parents constructor
    
    def consumption(self):
        Override consumption method. The method takes no input and returns 5.00 * weight
        
class Ship():
    def __init__(self, ID, currentPort, totalWeightCapacity, maxNumberOfAllContainers, maxNumberOfHeavyContainers, maxNumberOfRefrigeratedContainers,  maxNumberOfLiquidContainers, fuelConsumptionPerKM):
        constructor
    
    def getCurrentContainers(self):
        getter for containers attribute
    
    def sailTo(self, P):
        method that checks if the ship can successfully sail to the given destination port
        
    def refuel(self, fuelAdded):
        method adds fuel to the ship. It takes as an input representing the amount of added fuel and returns nothing
    
    def load(self, container):
        method checks if the given container can be successfully loaded to the ship.
    
    def unload(self, container):
        method checks if the given container can be successfully unloaded from a ship or not

@author: Rahul Thadhani
"""
import math

class Port:
    def __init__(self, ID, X, Y):
        self.ID = ID
        self.X = X
        self.Y = Y
        self.containers = []
        self.shipsHistory = []
        self.currentShips = []
    
    def setID(self, ID):
        self.ID = ID
    def setX(self, x):
        self.X = x
    def setY(self, y):
        self.Y = y
    def setContainer(self, contObj):
        self.containers.append(contObj)
    def setShipHistory(self, histObj):
        self.shipsHistory.append(histObj)
    def setCurrentShips(self, currentObj):
        self.currentShips.append(currentObj)
    
    def getID(self):
        return self.ID
    def getX(self):
        return self.X
    def getY(self):
        return self.Y
    def getContainer(self):
        return self.containers
    def getShipHistory(self):
        return self.shipsHistory
    def getCurrentShip(self):
        return self.currentShips
    
    def containerInPort(self, contObj):
        return contObj in self.getContainer()
    
    def removeCurrentShips(self, shipObj):
        if shipObj in self.getCurrentShip():
            self.currentShips.remove(shipObj)
            print("Ship successfully removed.")
        else:
            print("Ship not found.")
    
    def removeContainer(self, contObj):
        if contObj in self.getContainer():
            self.containers.remove(contObj)
            print("Ship successfully removed.")
        else:
            print("Ship not found.")
    
    def incomingShip(self, shipObj):
        if shipObj in self.getCurrentShip():
            print("Ship already exists.")
        else:
            self.currentShips.append(shipObj)
            print("Ship successfully added.")
    
    def outgoingShip(self, shipObj):
        if shipObj in self.getShipHistory():
            print("Ship already exists in history list.")
        else:
            self.shipsHistory.append(shipObj)
            print("Ship successfully added to history list.")
    
    def getDistance(self, portObj):
        return math.sqrt((self.X - portObj.X) ** 2 + (self.Y - portObj.Y) ** 2)

class Container:
    def __init__(self, ID, weight):
        self.ID = ID
        self.weight = weight
    
    def setID(self, ID):
        self.ID = ID
    def setWeight(self, weight):
        self.weight = weight
    
    def getID(self):
        return self.ID
    def getWeight(self):
        return self.weight
    
    def consumption(self):
        pass

class BasicContainer(Container):
    def __init__(self, ID, weight):
        super().__init__(ID, weight)
    
    def consumption(self):
        return 2.50 * self.getWeight()

class HeavyContainer(Container):
    def __init__(self, ID, weight):
        super().__init__(ID, weight)
    
    def consumption(self):
        return 3.00 * self.getWeight()

class LiquidContainer(HeavyContainer):
    def __init__(self, ID, weight):
        super().__init__(ID, weight)
    
    def consumption(self):
        return 4.00 * self.getWeight()

class RefrigeratedContainer(HeavyContainer):
    def __init__(self, ID, weight):
        super().__init__(ID, weight)
    
    def consumption(self):
        return 5.00 * self.getWeight()

class Ship():
    def __init__(self, ID, currentPort, totalWeightCapacity, maxNumberOfAllContainers, maxNumberOfHeavyContainers, maxNumberOfRefrigeratedContainers,  maxNumberOfLiquidContainers, fuelConsumptionPerKM):
        self.ID = ID
        self.fuel = 0.0
        self.currentPort = currentPort
        self.containers = []
        self.totalWeightCapacity = totalWeightCapacity
        self.maxNumberOfAllContainers = maxNumberOfAllContainers
        self.maxNumberOfHeavyContainers = maxNumberOfHeavyContainers
        self.maxNumberOfRefrigeratedContainers = maxNumberOfRefrigeratedContainers
        self.maxNumberOfLiquidContainers = maxNumberOfLiquidContainers
        self.fuelConsumptionPerKM = fuelConsumptionPerKM
        self.totalWeight = 0
        self.numberOfAllContainers = 0
        self.numberOfHeavyContainers = 0
        self.numberOfRefrigeratedContainers = 0
        self.numberOfLiquidContainers = 0
        
        self.currentPort.incomingShip(self)
    
    def getCurrentContainers(self):
        return self.containers
    
    def sailTo(self, P):
        distance = self.currentPort.getDistance(P)
        total_fuel_cost = (self.fuelConsumptionPerKM + sum(container.consumption() for container in self.containers)) * distance
        
        if total_fuel_cost <= self.fuel:
            self.fuel = self.fuel - total_fuel_cost
            self.currentPort.removeCurrentShips(self)
            self.currentPort.outgoingShip(self)
            P.incomingShip(self)
            self.currentPort = P
            return True
        else:
            return False
    
    def refuel(self, fuelAdded):
        self.fuel = self.fuel + fuelAdded
    
    def load(self, container):
        if (not self.currentPort.containerInPort(container)) or (self.numberOfAllContainers >= self.maxNumberOfAllContainers) or (self.totalWeight + container.getWeight() > self.totalWeightCapacity):
            return False
        elif isinstance(container, HeavyContainer):
            if self.numberOfHeavyContainers >= self.maxNumberOfHeavyContainers:
                return False
        elif isinstance(container, RefrigeratedContainer):
            if self.numberOfRefrigeratedContainers >= self.maxNumberOfRefrigeratedContainers:
                return False
        elif isinstance(container, LiquidContainer):
            if self.numberOfLiquidContainers >= self.maxNumberOfLiquidContainers:
                return False
        
        self.currentPort.removeContainer(container)
        self.containers.append(container)
        self.numberOfAllContainers = self.numberOfAllContainers + 1
        self.totalWeight = self.totalWeight + container.getWeight()
        if isinstance(container, HeavyContainer):
            self.numberOfHeavyContainers += 1
        elif isinstance(container, RefrigeratedContainer):
            self.numberOfRefrigeratedContainers += 1
        elif isinstance(container, LiquidContainer):
            self.numberOfLiquidContainers += 1
        
        return True
    
    def unload(self, container):
        if container not in self.containers:
            return False
        else:
            self.containers.remove(container)
            self.currentPort.containers.append(container)
            self.numberOfAllContainers -= 1
            self.totalWeight -= container.getWeight()
            if isinstance(container, HeavyContainer):
                self.numberOfHeavyContainers -= 1
            elif isinstance(container, RefrigeratedContainer):
                self.numberOfRefrigeratedContainers -= 1
            elif isinstance(container, LiquidContainer):
                self.numberOfLiquidContainers -= 1
            return True

def main():
    port1 = Port(300, 100.00, 200.00)
    port2 = Port(500, 120.60, 250.00)
    
    ship1 = Ship(1, port1, 140000, 100, 50, 40, 50, 34.00)
    ship2 = Ship(2, port1, 100000, 110, 60, 50, 30, 44.00)
    ship3 = Ship(3, port2, 110000, 120, 70, 60, 70, 23.00)
    
    container1 = HeavyContainer(1, 3500)
    container2 = BasicContainer(2, 500)
    container3 = LiquidContainer(3, 4500)
    container4 = RefrigeratedContainer(4, 5500)
    
    port1.containers.append(container1)
    port1.containers.append(container2)
    port2.containers.append(container3)
    port2.containers.append(container4)
    
    ship1.load(container1)
    ship2.load(container2)
    ship2.unload(container2)
    ship1.sailTo(port2)
    
    for ship in [ship1, ship2, ship3]:
        ship.refuel(370.74)

if __name__ == "__main__":
    main()
