class Membership:
    def __init__(self, level):
        self.level = level
        self.benefits = {
            "ExtraBaggage": False,
            "BonusMile_25%": False,
            "BonusMile_50%": False,
            "PriorityBoarding":False,
            "LoungeAccessWithoutHospitality" : False,
            "LoungeAccessWithHospitality": False,
        }

    def getLevel(self):
        return self.level
    
    def setLevel(self, level):
        self.level = level

    def getBenefits(self):
        return self.benefits
    
    def addBenefits(self, benefit):
        self.benefits[benefit] = True
        return self.benefits

    def removeBenefits(self, benefit):
        if benefit in self.benefits.keys():
            del self.benefits[benefit]