from membership import Membership
from flight import Flight

class Passenger:
    def __init__(self, name, id, seatclass, membership:Membership, flight:Flight):
        self.seatclass = seatclass
        self.name = name
        self.miles = 0
        self.id = id
        self.membership = membership
        self.flight = flight

    def getMembership(self):
        return self.membership

    def setMembership(self, membership):
        self.membership = membership

    def getFlight(self):
        return self.flight

    def setFlight(self, flight):
        self.flight = flight
    
    def getSeatClass(self):
        return self.seatclass

    def setSeatClass(self, seatclass):
        self.seatclass = seatclass

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getMiles(self):
        return self.miles

    def calculateMiles(self):
        membershipLevel = self.membership.getLevel()
        distance = self.flight.getDistance()
        seat = self.getSeatClass()
        # Basic membership level
        if membershipLevel == 'basic':
            if seat == 'economy':
                temp = distance * 0.50
                self.miles = temp
            elif seat == 'Business':
                self.miles = distance
            else: 
                return False
        # silver membership level
        elif membershipLevel == 'silver':
            if seat == 'economy':
                temp = distance * 0.75
                self.miles = temp
            elif seat == 'Business':
                temp = distance * 1.25
                self.miles = temp
            else: 
                return False
        # gold membership level
        elif membershipLevel == 'gold':
            if seat == 'economy':
                self.miles = distance
            elif seat == 'Business':
                temp = distance * 1.50
                self.miles = temp
            else: 
                return False
        else:
            return False

    def getFreeTicket(self):
        inter = 0
        dom = 0
        while self.miles >= 9000:
            if self.miles >= 10000:
                inter += 1
            
            elif self.miles >= 9000 :
                dom += 1
        return f"You can get {inter} international flights, and {dom} domestic flight for free!"