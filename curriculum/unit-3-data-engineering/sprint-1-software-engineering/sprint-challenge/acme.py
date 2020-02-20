import random as rd

"""Class for creating various products following a general template
"""


class Product:
    """Creates and initializes the variables for a product and assigns a unique
    identifier

    Args
    ----
    name: type(str), no default
    price: type(int), default=10
    weight: type(int), default=20
    flammability: type(float), default=0.5

    Automatically Assigned
    ----------------------
    identifier: type(int), automatically generated random
    number from 1,000,000 to 9,999,999
    """

    def __init__(self, name, price=10, weight=20,
                 flammability=0.5, identifier=rd.randint(1000000, 10000000)):

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """Method for determining the likelihood of theft for a product

        Args
        ----
        self
        Returns
        -------
        str: The likelihood of theft of a product
        based on the ratio of price to weight"""

        likelihood = self.price / self.weight

        if likelihood < 0.5:
            return "Not so stealable..."
        elif likelihood < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        """Method for determining the likelihood of theft for a product

        Args
        ----
        self
        Returns
        -------
        str: The likelihood of an explosion of a product based on
        the product of flammability and weight"""

        reac = self.flammability * self.weight

        if reac < 10:
            return "...fizzle."
        elif reac < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    """Subclass of Product
    A Boxing Glove"""

    def __init__(self, name):
        super(BoxingGlove, self).__init__(name)
        self.weight = 10

    def explode(self):
        """Alters the return of the parent class to reflect
        the attributes of the child class

        Args
        ----
        self

        Returns
        -------
        a statement of the product being a glove
        """

        return "...it's a glove."

    def punch(self):
        """ Method for determining the discomfort resulting
        from punching based on it's weight

        Args
        ----
        self

        Returns
        ----
        The resulting feeling of punching using the glove
        """

        if self.weight < 5:
            return "That tickles."
        elif self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
