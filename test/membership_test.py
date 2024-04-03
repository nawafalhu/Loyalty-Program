from membership import Membership

class test_membership:
    def test_level_set_get():
        membership = Membership('silver')
        assert membership.getLevel() == 'silver'

    def add_benefits_test():
        membership = Membership("Gold")
        membership.addBenefits("ExtraBaggage")
        assert membership.getBenefits("ExtraBaggage") == True

    def remove_benefits_test():
        membership = Membership("silver")
        membership.removeBenefits("ExtraBaggage")
        assert membership.getBenefits("ExtraBaggage") == False