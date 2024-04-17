from flight import Flight
from membership import Membership
from membership import FreeDomesticFlightTicket, FreeInternationalFlightTicket
from membership import addExtraLuggage, udgradeSeat

class Booking:
    def __init__(self, flight:Flight, membership: Membership):
        self.flight = flight
        self.membership = membership
        self.bookings = []

    def processOnlineBooking(self):
        return 0

    def processMilesBooking(self):
        if self.flight.type == 'Domestic':
            reward = FreeDomesticFlightTicket()
            reward.redeem(self.membership)
            self.bookings.append(Booking(self.flight, self.membership))
            return "Booking Success"
        
        elif self.flight.type == 'International':
            reward = FreeInternationalFlightTicket()
            reward.redeem(self.membership)
            self.bookings.append(Booking(self.flight, self.membership))
            return "Booking Success"
        
    def addLuggage(self):
        reward = addExtraLuggage()
        reward.redeem(self.membership, self.flight)
        return "ُExtra Luggage added"

    def upgrade(self):
        reward = udgradeSeat()
        reward.redeem(self.membership, self.flight)
        return "Seat Upgraded"
    
    def addBooking(self, paymentMethod):
        if paymentMethod == 'online':
            self.processOnlineBooking()        
        else :
            self.processMilesBooking()



