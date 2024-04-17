from book import Booking
from flight import Flight
from membership import Membership


def test_booking_with_miles():
    flight = Flight('SA123', 134341223, 'Domestic', 'economy', False)
    memb = Membership('silver', flight)
    booking = Booking(flight, memb)
    
    result = booking.processMilesBooking()

    assert 'Booking Success' in result

def test_upgrade_busines_seat():
    flight = Flight('SA123', 134341223, 'Domestic', 'business', False)
    memb = Membership('silver', flight)
    booking = Booking(flight, memb)

    result = booking.upgrade()
    assert 'Not Enough Miles or You have Business seat already' in result

def test_add_extra_luggage_twice():
    flight = Flight('SA123', 1345334341223, 'Domestic', 'business', addExtraLuggage=False)
    memb = Membership('silver', flight)
    booking = Booking(flight, memb)

    result1 = booking.addLuggage()
    result2 = booking.addLuggage()

    assert 'Extra Luggage added' in result1
    assert 'Not Enough Miles or You have Extra Luggage already' in result2

def test_add_extra_luggage_not_enough_miles():
    flight = Flight('SA123', 3453453345334534345345, 'Domestic', 'business', False)
    memb = Membership('silver', flight)
    booking = Booking(flight, memb)

    result = booking.addLuggage()
    assert 'Not Enough Miles or You have Extra Luggage already'

def test_upgrade_seat():
    flight = Flight('SA123', 1345334341223, 'Domestic', 'economy', addExtraLuggage=False)
    memb = Membership('silver', flight)
    booking = Booking(flight, memb)

    result = booking.upgrade()
    assert 'Seat Upgraded' in result

