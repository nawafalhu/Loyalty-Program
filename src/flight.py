class Flight:
    def __init__(self, flightNumber, departure, destination, distance, departureTime, arrivalTime):
        self.flightNumber = flightNumber
        self.departure = departure
        self.destination = destination
        self.distance = distance
        self.departureTime = departureTime
        self.arrivalTime = arrivalTime
    
    def getFlightNumber(self):
        return self.flightNumber

    def getDeparture(self):
        return self.departure

    def getDestination(self):
        return self.destination
    
    def getDistance(self):
        return self.distance

    def getDepartureTime(self):
        return self.departureTime

    def getArrivalTime(self):
        return self.arrivalTime