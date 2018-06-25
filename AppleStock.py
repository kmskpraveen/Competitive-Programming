# def get_max_profit(stock_prices):

#     # Calculate the max profit
    
#     profit = -1*max(stock_prices)
    
#     for i in range(len(stock_prices)):
#         for j in range(i,len(stock_prices)):
#             if(profit<=stock_prices[j]-stock_prices[i]) and i!=j:
#                 profit = stock_prices[j]-stock_prices[i]
    
#     if profit == -1*max(stock_prices):
#         raise Exception

#     return profit
    
    
def get_max_profit(stock_prices):

    # Calculate the max profit
    
    min = stock_prices[0]
    profit = stock_prices[1]-stock_prices[0]
    
    for i in stock_prices[1:]:
        if profit <= i-min:
            profit = i-min
        if min >= i:
            min = i
        
    return profit    


















# Tests

import unittest

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_one_price_raises_error(self):
        with self.assertRaises(Exception):
            get_max_profit([1])

    def test_empty_list_raises_error(self):
        with self.assertRaises(Exception):
            get_max_profit([])

unittest.main(verbosity=2)