from lib2to3.pgen2 import driver
from tdd_1.logic import Cafe

def test_should_return_tea_and_change_30_baht_when_buying_tea_with_50_baht():
  cafe = Cafe()
  drink, change = cafe.buy("tea",50.0)
  assert (drink, change) == ("tea", 30.0)