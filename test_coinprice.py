import unittest
from unittest import TestCase
from unittest.mock import patch

import coinprice

class TestCoinprice(TestCase):

    @patch('coinprice.request_rates')
    def test_bitcoin_to_dollars(self, mock_rates):
        mock_rate = 5678.9012
        example_api_response = {'time': {''}, 'disclaimer': 'This data was a test', 'bpi':{'USD': {'code':'USD', 'rate_float':mock_rate}, 'EUR': {'code':'EUR', 'rate_float':'8080.80'}}}
        mock_rates.side_effect = [example_api_response]
        converted = coinprice.convert_dollars_to_bitcoin(100)
        self.assertEqual(567890.12, converted)

if __name__ == '__main__':
    unittest.main()