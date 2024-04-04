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
        return self.years

    def upgradeLevel(self):
        if self.level == "basic":
            self.level = "silver"
            return True

        elif self.level == "silver":
            self.level = "gold"
            return True

        elif self.level == "gold":
            return False    
        else :
            return False
    
    def addBenefits(self, benefit):
        self.benefits[benefit] = True
        return self.benefits

    def removeBenefits(self, benefit):
        if benefit in self.benefits.keys():
            del self.benefits[benefit]