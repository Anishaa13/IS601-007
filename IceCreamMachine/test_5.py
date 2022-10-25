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
    machine.flavors[0].quantity=2
    machine.handle_container("waffle cone")
    machine.handle_flavor("chocolate")
    machine.handle_flavor("next")
    machine.handle_toppings("gummy bears")
    machine.handle_toppings("peanuts")
    machine.handle_toppings("done")
    return machine

def test_production_line(first_order):
    return first_order is None

#Test 5