from abc import ABC, abstractmethod

class Reward(ABC):
    @abstractmethod
    def FreeDomesticFlightTicket(self, miles):
        if miles >= 9000:
            return True
        return False

    @abstractmethod
    def FreeInternationalFlightTicket(self, miles):
        if miles >= 10000:
            return True
        return False
    
    @abstractmethod
    def udgradeSeat(self):
        pass

    @abstractmethod
    def addExtraBaggage(self):
        pass

# basic level
class basic(Reward):
    def udgradeSeat(self, miles):
        if miles >= 3000:
            return True
        return False

    def addExtraBaggage(self, miles):
        if miles >= 1500:
            return True
        return False

# silver level
class silver(Reward):    
    def udgradeSeat(self, miles):
        if miles >= 2500:
            return True
        return False

    def addExtraBaggage(self, miles):
        if miles >= 1000:
            return True
        return False

# gold level
class gold(Reward):
    def udgradeSeat(self, miles):
        if miles >= 2000:
            return True
        return False

    def addExtraBaggage(self, miles):
        if miles >= 500:
            return True
        return False
