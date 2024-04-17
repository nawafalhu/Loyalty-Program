from abc import ABC, abstractmethod
from flight import Flight

class Membership:
    def __init__(self, level, flight:Flight):
        self.level = level
        self.flight = flight
        self.miles = 0
        self.tierMiles = 0

    def calculateTotalMiles(self):
        distance = self.flight.distance
        seat = self.flight.seatclass
 
        # Basic membership level
        if self.level == 'basic':
            if seat == 'economy':
                temp = distance * 0.50
                return temp
            elif seat == 'Business':
                return distance 
            else: 
                return 0
            
        # silver membership level
        elif self.level == 'silver':
            if seat == 'economy':
                temp = distance * 0.75
                return temp
            elif seat == 'Business':
                temp = distance * 1.25
                return temp
            else: 
                return 0
            
        # gold membership level
        elif self.level == 'gold':
            if seat == 'economy':
                return distance
            elif seat == 'Business':
                temp = distance * 1.50
                return temp
            else: 
                return 0
        else:
            return 0

    def getRequiredPointsFor(self, reward):
        # Free Domestic flight
        if reward == "FreeDomestic":
            return 9000
        
        # Free Internationa flight
        elif reward == "FreeInternationa":
            return 10000
        
        # udgrade Seat
        elif reward == "udgradeSeat":
            if self.level == "basic":
                return 2000
            elif self.level == "silver":
                return 2500
            elif self.level == "gold":
                return 3000
        
        # add Extra Baggage
        elif reward == "addExtraLuggage":
            if self.level == "basic":
                return 500
            elif self.level == "silver":
                return 1000
            elif self.level == "gold":
                return 1500
            

class Reward(ABC):
    @abstractmethod
    def redeem(self, membership):
        pass

# Free Domestic Flight Ticket
class FreeDomesticFlightTicket(Reward):
    def redeem(self, membership:Membership):
        point = membership.getRequiredPointsFor("FreeDomestic")
        miles = membership.calculateTotalMiles()
        membership.tierMiles += miles

        if miles >= point:
            miles -= point
            self.miles = miles
            return True
        return 'Not Enough Miles'
            


# Free International Flight Ticket
class FreeInternationalFlightTicket(Reward):
    def redeem(self, membership:Membership, flight):
        point = membership.getRequiredPointsFor("FreeInternational")
        miles = membership.calculateTotalMiles()
        membership.tierMiles += miles

        if miles >= point:
            miles -= point
            self.miles = miles
            return True
        return 'Not Enough Miles'

# udgrade Seat
class udgradeSeat(Reward):
    def redeem(self, membership:Membership, flight):
        point = membership.getRequiredPointsFor("udgradeSeat")
        miles = membership.calculateTotalMiles()
        membership.tierMiles += miles

        if miles >= point and flight.seatclass != 'Business':
            miles -= point
            self.miles = miles

            flight.seatclass = 'Business'
            return True
        return 'Not Enough Miles or You have Business seat already'

# add Extra Baggage
class addExtraLuggage(Reward):
    def redeem(self, membership:Membership, flight):
        point = membership.getRequiredPointsFor("addExtraLuggage")
        miles = membership.calculateTotalMiles()
        membership.tierMiles += miles

        if miles >= point and flight.addExtraLuggage == False:
            miles -= point
            self.miles = miles

            flight.addExtraLuggage = True
            return True
        return 'Not Enough Miles or You have Extra Luggage already'

