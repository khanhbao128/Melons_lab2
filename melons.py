"""Classes for melon orders."""

class AbstractMelonOrder():

    def __init__(self, species, qty, country_code=None):

        self.species = species
        self.qty = qty
        self.shipped = False
        if country_code:
            self.country_code = country_code
    
    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "christmas":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international":
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        
        # self.species = species
        # self.qty = qty
        # self.shipped = False
        

        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, country_code)#, country_code)
        # self.species = species
        # self.qty = qty
        # self.shipped = False
        # self.order_type = "international"
        

        self.tax = 0.17


    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):

    passed_inspection = False


    def __init__(self, species, qty):
        super().__init__(species, qty)

        self.tax = 0


    def pass_inspection(self, passed_inspection):

        self.passed_inspection = passed_inspection

