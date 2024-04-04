class Flight:
    def __init__(self, flightNumber, departure, destination, departureTime, arrivalTime):
        self.flightNumber = flightNumber
        self.departure = departure
        self.destination = destination
        self.departureTime = departureTime
        self.arrivalTime = arrivalTime
    
    def getFlightNumber(self):
        return self.flightNumber

    def getDeparture(self):
        return self.departure

    def getDestination(self):
        return self.destination

    def getDepartureTime(self):
        return self.departureTime

    def getArrivalTime(self):
        return self.arrivalTime