from src.flight import Flight

flight = Flight("SA112", "RUH", "NYC", 11100, "1:00PM", "2:30AM")

def get_flight_test():
    assert flight.getFlightNumber() == "SA112"

def get_Departure_test():
    assert flight.getDeparture() == "RUH"

def get_Destination_test():
    assert flight.getDestination() == "NYS"

def get_DepartureTime_test():
    assert flight.getDepartureTime() == "1:00PM"

def get_ArrivalTime_test():
    assert flight.getArrivalTime() == "2:30AM"

def get_Distance_test():
    assert flight.getDistance() == 11100