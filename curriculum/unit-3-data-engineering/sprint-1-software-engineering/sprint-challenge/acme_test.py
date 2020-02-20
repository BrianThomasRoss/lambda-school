import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_price(self):
        """test default price functions correctly"""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_weight(self):
        '''test default weight'''
        test = Product('Test Product')
        self.assertEqual(test.weight, 20)

    def test_new_product(self):
        '''Test to ensure correct instantion of a new product'''
        test = Product('New Product', 9, 27, 1)
        self.assertEqual(test.stealability(), 'Not so stealable...')
        self.assertEqual(test.explode(), '...boom!')


class AcmeReportTests(unittest.TestCase):
    '''Making sure Acme report is correct '''
    def test_default_num_products(self):
        ''' Testing if product generator making default amount'''
        num_prod = generate_products()
        self.assertEqual(len(num_prod), 30)

    def test_legal_names(self):
        '''Testing if adjective and nouns are the only string in products'''
        prod_names = generate_products()

        for product in prod_names:
            prod_name = product.name.split()
            adjective = prod_name[0]
            noun = prod_name[1]
            self.assertIn(adjective, ADJECTIVES)
            self.assertIn(noun, NOUNS)


if __name__ == '__main__':
    unittest.main()
