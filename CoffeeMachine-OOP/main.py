#from menu import Menu, MenuItem
import menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main_coffee():
    jazz_coffee_menu = menu.Menu()
    jazz_coffee_machine = CoffeeMaker()
    jazz_money_machine = MoneyMachine()

    machine_operational = True

    while machine_operational :
        drink_choice =input(f"What would you like? {jazz_coffee_menu.get_items()}")
        if drink_choice == "off":
            machine_operational = False
        elif drink_choice == "report":
            jazz_coffee_machine.report()
            jazz_money_machine.report()
        else:
            drink_selected = jazz_coffee_menu.find_drink(drink_choice)
            if jazz_coffee_machine.is_resource_sufficient(drink_selected):
                jazz_money_machine.make_payment(drink_selected.cost)
                jazz_coffee_machine.make_coffee(drink_selected)
                jazz_money_machine.report()
            else:
                machine_operational = False


main_coffee()



