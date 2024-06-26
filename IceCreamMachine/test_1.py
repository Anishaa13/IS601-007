import pytest
from IcecreamMachine import IceCreamMachine

@pytest.fixture
def machine():
    icm = IceCreamMachine()
    return icm

#Test 1 - container must be the first selection (can't add flavors/toppings without a container choice)
#UCID: as4283, Date: 10/23/2022
def test_first_selection(machine):
    machine.handle_container("cup")
    machine.handle_flavor("strawberry")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("m&ms")
    machine.handle_toppings("peanuts")
    
    y = machine.inprogress_icecream[0]
    return y in ["waffle cone", "sugar cone", "cup"]  

#Test 1