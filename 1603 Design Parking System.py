#https://leetcode.com/problems/design-parking-system/description/

class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType):
        self.carType = carType
        if self.carType == 1 and self.big > 0:
            self.big -= 1
            return True
        if self.carType == 2 and self.medium > 0:
            self.medium -= 1
            return True
        if self.carType == 3 and self.small > 0:
            self.small -= 1
            return True
