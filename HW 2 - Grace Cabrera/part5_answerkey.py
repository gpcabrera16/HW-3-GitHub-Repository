"""
Calculate the number of pizzas needed for the club meeting. 
"""

import math

SLICES_PER_PIZZA = 8
BUDGET = 75
PRICE_PER_PIZZA = 15

def calculate_pizzas(number_members, slices_per_person):
    """
    Calculate the number of pizzas needed for the first club meeting.

    Inputs:
        number_members: expected number of participants
        slices_per_person: number of slices that each person will eat

    Outputs:
        number of whole pizzas needed
    """
    total_slices = number_members * slices_per_person
    pizzas_needed = math.ceil(total_slices / SLICES_PER_PIZZA)
    return pizzas_needed

def calculate_cost(pizzas_needed):
    """
    Calculate the total cost for the pizza order

    Input:
        pizzas_needed: number of pizzas being ordered

    Output:
        total cost of the pizzas
    """
    total_cost = pizzas_needed * PRICE_PER_PIZZA
    return total_cost

def check_budget(total_cost):
    """
    Make sure the pizza order is within the club budget

    Input:
        total_cost: total cost of the pizza order

    Output:
        statement whether order is within budget
    """
    if total_cost <= BUDGET:
        money_left = BUDGET - total_cost
        return f"The order is within budget. You will have ${money_left: } left."
    else:
        amount_over = total_cost - BUDGET
        return f"The order is ${amount_over: } over budget."

if __name__ == '__main__':
    number_members = int(input("How many members are attending? "))
    slices_per_person = int(input("How many slices will each person eat? "))

    if number_members <= 0:
        print("The number of members must be greater than 0.")
    elif slices_per_person <= 0:
        print("Slices per person must be greater than 0.")
    else:
        pizzas_needed = calculate_pizzas(number_members, slices_per_person)

        total_cost = calculate_cost(pizzas_needed)

        print(f"You should order {pizzas_needed} pizzas.")
        print(f"The total cost will be ${total_cost: }.")
        print(check_budget(total_cost))