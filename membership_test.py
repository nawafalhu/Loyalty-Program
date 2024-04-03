from membership import Membership
import pytest

def test_level_set_get():
    membership = Membership('silver')
    assert membership.getLevel() == 'silver'

def add_benefits_test():
    pass

def remove_benefits_test():
    pass