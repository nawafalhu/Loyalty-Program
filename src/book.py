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
        pass

    def addBooking(self, flight, paymentMethod):
        if paymentMethod == 'online':
            self.processOnlineBooking(flight)        
        else:
            self.processMilesBooking(flight)

    def processMilesBooking(self, flight):
        if flight.self.type == 'Domestic':
            reward = FreeDomesticFlightTicket()
            reward.redeem(self.membership)
            self.bookings.append(Booking())
            return "Booking Success"
        
        elif flight.self.type == 'Internationa':
            reward = FreeInternationalFlightTicket()
            reward.redeem(self.membership)
            self.bookings.append(Booking)
            return "Booking Success"
        
    def addLuggage(self):
        reward = addExtraLuggage()
        reward.redeem(self.membership)
        return "ُExtra Luggage added"

    def upgrade(self):
        reward = udgradeSeat()
        reward.redeem(self.membership)
        return "Seat Upgraded"



