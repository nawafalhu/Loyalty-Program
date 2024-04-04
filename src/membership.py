class Membership:
    def __init__(self, level, years):
        self.level = level
        self.years = years
        self.benefits = {
            "PriorityBoarding":False,
            "LA" : False, # LoungeAccessWithoutHospitality
            "LAWH": False, # # LoungeAccessWithHospitality
        }
        if self.level == 'silver':
            self.benefits['LA'] = True
        elif self.level == 'gold':
            self.benefits['LAWH'] = True
            self.benefits['PriorityBoarding'] = True

    def getLevel(self):
        return self.level
    
    def setLevel(self, level):
        self.level = level

    def getBenefits(self, benefit):
        return self.benefits[benefit]
    
    def getyears(self):
        return self.years

    def removeBenefits(self, benefit):
        if benefit in self.benefits.keys():
            del self.benefits[benefit]