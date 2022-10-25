from importlib import machinery
import pytest
from IcecreamMachine import STAGE, Flavor, IceCreamMachine, Toppings


@pytest.fixture
def machine():
    icm = IceCreamMachine()
    return icm
#UCID: as4283, Date: 10/23/2022
@pytest.fixture
def first_order(machine):
    machine.toppings[0].quantity=2
    machine.handle_container("cup")
    machine.handle_flavor("strawberry")
    machine.handle_flavor("next")
    machine.handle_toppings("gummy bears")
    machine.handle_toppings("m&ms")
    return machine

def test_production_line(first_order):
    return first_order is not None

#Test 3