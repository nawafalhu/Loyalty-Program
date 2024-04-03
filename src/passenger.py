from membership import Membership


class Passenger:
    def __init__(self, name, id, membership:Membership):
        self.name = name
        self.membershipLevel = membership
        self.miles = 0
        self.id = id

    def getMembershipLevel(self):
        pass

    def setMembershipLevel(self, level):
        pass

    def getMiles(self):
        pass

    def addMiles(self, miles):
        pass

    def redeemMiles(self, miles):
        pass

    def getFreeTicket(self):
        pass

    