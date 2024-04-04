from abc import ABC, abstractmethod

class Reward(ABC):
    @abstractmethod
    def redeem(self, membership):
        pass

# basic level
class FreeDomesticFlightTicket(Reward):
    def redeem(self, membership):
        member = membership.getRequiredPointsFor("FreeDomestic")


# silver level
class FreeInternationalFlightTicket(Reward):
    def redeem(self, membership):
        pass

# gold level
class udgradeSeat(Reward):
    def redeem(self, membership):
        pass

class addExtraBaggage(Reward):
    def redeem(self, membership):
        pass

