from membership import Membership


def level_set_get_test():
    membership = Membership('silver')
    membership.setLevel("gold")
    assert membership.getLevel() == 'gold'

def add_benefits_test():
    membership = Membership("Gold")
    membership.addBenefits("ExtraBaggage")
    assert membership.getBenefits("ExtraBaggage") == True

def remove_benefits_test():
    membership = Membership("silver")
    membership.removeBenefits("ExtraBaggage")
    assert membership.getBenefits("ExtraBaggage") == False

def Upgrade_level_test():
    membership = Membership("gold", 3)
    assert membership.upgradeLevel() == False

def getyear_test():
    membership = Membership("silver", 2)
    assert membership.getyears() == 2
