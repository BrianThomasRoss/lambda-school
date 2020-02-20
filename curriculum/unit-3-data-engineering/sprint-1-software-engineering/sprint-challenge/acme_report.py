import random
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    """Generates a list of randomly produced products

    Args
    ----
    num_products: type(int) - default=30

    Returns
    -------
    products: list of randomly created products"""
    products = []
    lower_bound = 5
    upper_bound = 100
    for item in range(num_products):

        name = f'{random.sample(ADJECTIVES, 1)[0]} {random.sample(NOUNS, 1)[0]}'

        price = random.randint(lower_bound, upper_bound + 1)
        weight = random.randint(lower_bound, upper_bound + 1)
        flammability = random.uniform(0, 2.5)
        products.append(Product(name, price, weight, flammability))

    return products


def inventory_report(products):
    """Generates an inventory report containing summary statistics of products

    Args
    ----
    products: list object

    Returns
    ------
    summary statistics of the product list passed
    """
    def ave(lst):
        aver = sum(lst) / len(lst)
        return aver

    names = set([p.name for p in products])
    len_prod = len(names)

    average_price = ave([p.price for p in products])
    average_weight = ave([p.weight for p in products])
    average_flammability = ave([p.flammability for p in products])

    print ('   ACME CORPORATION OFFICIAL INVENTORY REPORT' +"\n" + 
    "~*~*~"*10 + "\n" +
    '       Unique product names:' + f" {len_prod}" + "\n" +
    '       Average price:' + f" {average_price:.2f}" + "\n" + 
    '       Average weight:' +  f" {average_weight:.2f}" + "\n" +
    '       Average flammability:' + f" {average_flammability:.2f}" + "\n" +
     "~*~*~"*10 + "\n" + "               END REPORT")

if __name__ == '__main__':
    inventory_report(generate_products())
