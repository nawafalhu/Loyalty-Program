from src.passenger import Passenger
from src.flight import Flight
from src.membership import Membership

membership = Membership("silver", 2)
flight = Flight("SA112", "RUH", "NYC", 11100, "1:00PM", "2:30AM")
passenger = Passenger("nawaf", 1122, "economy", membership, flight)

def get_set_SeatClass_test():
    assert passenger.getSeatClass() == "economy"
    assert passenger.setSeatClass("business") == "business"

def get_name_id_miles_test():
    assert passenger.getId() == 1122
    assert passenger.getName() == "nawaf"
    assert passenger.getMiles() == 0

def calculate_miles_test():
    assert passenger.calculateMiles() == 11100 * 0.75

def get_FreeTicket_test():
    passenger.calculateMiles()
    assert passenger.getFreeTicket() == "You can get 0 international flights, and 0 domestic flight for free!"