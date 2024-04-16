from membership import Membership


class Passenger:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.benefits = {
            "FreeDomestic":False,
            "FreeInternational": False,
            "udgradeSeat": False,
            "addExtraBaggage":False
        }
     
    def addBenefits(self, benefit):
        if benefit in self.benefits.keys():
            self.benefits[benefit] = True
            return True
        return False

    
        