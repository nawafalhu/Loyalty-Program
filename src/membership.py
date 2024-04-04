from abc import ABC, abstractmethod

class Membership:
    def __init__(self, level, years):
        self.level = level
        self.years = years
        self.benefits = {
            "PriorityBoarding":False,
            "LA" : False, # LoungeAccessWithoutHospitality
            "LAWH": False, # # LoungeAccessWithHospitality
        }
        if self.level == 'silver':
            self.benefits['LA'] = True
        elif self.level == 'gold':
            self.benefits['LAWH'] = True
            self.benefits['PriorityBoarding'] = True

    def getLevel(self):
        return self.level
    
    def setLevel(self, level):
        self.level = level

    def getBenefits(self, benefit):
        return self.benefits[benefit]
    
    def getyears(self):
        return self.years

    def removeBenefits(self, benefit):
        if benefit in self.benefits.keys():
            del self.benefits[benefit]

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
        elif reward == "addExtraBaggage":
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

# basic level
class FreeDomesticFlightTicket(Reward):
    def redeem(self, membership):
        point = membership.getRequiredPointsFor("FreeDomestic")



# silver level
class FreeInternationalFlightTicket(Reward):
    def redeem(self, membership):
        point = membership.getRequiredPointsFor("FreeInternational")

# gold level
class udgradeSeat(Reward):
    def redeem(self, membership):
        point = membership.getRequiredPointsFor("udgradeSeat")

class addExtraBaggage(Reward):
    def redeem(self, membership):
        point = membership.getRequiredPointsFor("addExtraBaggage")

