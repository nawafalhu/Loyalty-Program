class Membership:
    def __init__(self, level, years):
        self.level = level
        self.years = years
        self.benefits = {
            "ExtraBaggage": False,
            "BonusMile_25%": False,
            "BonusMile_50%": False,
            "PriorityBoarding":False,
            "LA" : False, # LoungeAccessWithoutHospitality
            "LAWH": False, # # LoungeAccessWithHospitality
        }

    def getLevel(self):
        return self.level
    
    def setLevel(self, level):
        self.level = level

    def getBenefits(self, benefit):
        return self.benefits[benefit]
    
    def getyears(self):
        pass

    def upgradeLevel(self, level):
        pass
    
    def addBenefits(self, benefit):
        self.benefits[benefit] = True
        return self.benefits

    def removeBenefits(self, benefit):
        if benefit in self.benefits.keys():
            del self.benefits[benefit]