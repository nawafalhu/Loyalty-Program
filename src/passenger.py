from membership import Membership


class Passenger:
    def __init__(self, name, id, membership):
        self.name = name
        self.membershipLevel = membership
        self.miles = 0
        self.id = id

    def getMembershipLevel(self):
        pass

    def setMembershipLevel(self, level):
        pass

    