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


class basic(Reward):
    def udgradeSeat(self, miles):
        if miles >= 3000:
            return True
        return False

    def addExtraBaggage(self, miles):
        if miles >= 1500:
            return True
        return False


class silver(Reward):    
    def udgradeSeat(self):
        pass

    def addExtraBaggage(self):
        pass


class gold(Reward):
    def udgradeSeat(self):
        pass

    def addExtraBaggage(self):
        pass
