from importlib import machinery
import pytest
from IcecreamMachine import STAGE, Flavor, IceCreamMachine, Toppings

#UCID: as4283, Date: 10/23/2022
@pytest.fixture
def machine():
    icm = IceCreamMachine()
    return icm

@pytest.fixture
def first_order(machine):
    machine.handle_container("waffle cone")
    machine.handle_flavor("chocolate")
    machine.handle_flavor("next")
    machine.handle_toppings("sprinkles")
    machine.handle_toppings("done")
    machine.handle_pay(2.25,"2.25")
    return machine
#UCID: as4283, Date: 10/23/2022
@pytest.fixture
def second_order(first_order, machine):
    machine.handle_container("cup")
    machine.handle_flavor("starwberry")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("peanuts")
    machine.handle_toppings("done")
    machine.handle_pay(3.25,"3.25")
    return machine

@pytest.fixture
def third_order(second_order, machine):
    machine.handle_container("waffle cone")
    machine.handle_flavor("chocolate")
    machine.handle_flavor("next")
    machine.handle_toppings("peanuts")
    machine.handle_toppings("m&ms")
    machine.handle_toppings("done")
    machine.handle_pay(2.5,"2.5")
    return machine

def test_production_line(third_order):
    assert third_order.total_sales==8.0