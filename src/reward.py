from abc import ABC, abstractmethod

class Reward(ABC):
    @abstractmethod
    def redeem(self, membership):
        pass

# basic level
class FreeDomesticFlightTicket(Reward):
    def redeem(self, membership):
        pass


# silver level
class FreeInternationalFlightTicket(Reward):
    def redeem(self, membership):
        pass

# gold level
class udgradeSeat(Reward):
    def redeem(self, membership):
        pass




# FreeDomesticFlightTicket
# FreeInternationalFlightTicket
# udgradeSeat
# addExtraBaggage