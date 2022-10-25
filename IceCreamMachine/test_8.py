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
    machine.handle_container("cup")
    machine.handle_flavor("chocolate")
    machine.handle_flavor("next")
    machine.handle_toppings("peanuts")
    machine.handle_toppings("done")
    #assert machine.calculate_cost() == 2.25 
    machine.handle_pay(2.25,"2.25")
    return machine
    #assert first_order.total_icecreams==1
#UCID: as4283, Date: 10/23/2022
@pytest.fixture
def second_order(first_order, machine):
    machine.handle_container("cup")
    machine.handle_flavor("strawberry")
    machine.handle_flavor("next")
    machine.handle_toppings("peanuts")
    machine.handle_toppings("done")
    #assert machine.calculate_cost() == 3.25
    machine.handle_pay(3.25,"3.25")
    return machine
    #assert second_order.total_icecreams==2
#UCID: as4283, Date: 10/23/2022
@pytest.fixture
def third_order(second_order, machine):
    machine.handle_container("cup")
    machine.handle_flavor("chocolate")
    machine.handle_flavor("next")
    machine.handle_toppings("peanuts")
    machine.handle_toppings("done")
    #assert machine.calculate_cost() == 2.5
    machine.handle_pay(2.5,"2.5")
    return machine
    #assert third_order.total_icecreams==3

def test_production_line(second_order):
    assert second_order.total_icecreams==2

def test_production_line_next(third_order):
    assert third_order.total_icecreams==3