import unittest
from international_address_formatter import AddressFormatter

class TestAddressFormatterGermany(unittest.TestCase):

    def test_street(self):
        formatter = AddressFormatter()
        self.assertEqual(
            "Bahnhofstr. 10, 86150 Augsburg, Germany",
            formatter.one_line({
                'road': "Bahnhofstr.",
                'house_number': "10",
                'postcode': "86150",
                'city': "Augsburg",
                'state': "Bayern",
                'country': "Germany"
            }, country='DE')
        )

if __name__ == '__main__':
    unittest.main()