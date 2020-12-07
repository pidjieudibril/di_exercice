def make_pizza(size, *toppings):
    """
    Summarize the pizza we are about to make.
    """
    print("\nMaking a {}-inch pizza with the following toppings:".format(size))
    for topping in toppings:
        print("- " + topping)