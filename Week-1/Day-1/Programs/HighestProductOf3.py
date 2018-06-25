import unittest


# def highest_product_of_3(list_of_ints):

#     list_of_ints.sort()
    

#     return list_of_ints[len(list_of_ints)-1]*list_of_ints[len(list_of_ints)-2]*list_of_ints[len(list_of_ints)-3 ]

def highest_product_of_3(list_of_ints):

    if (len(list_of_ints) < 3):
        raise Exception

    else:
        high = max(list_of_ints[0], list_of_ints[1])
        low  = min(list_of_ints[0], list_of_ints[1])

        high_prod_2 = list_of_ints[0] * list_of_ints[1]
        low_prod_2  = list_of_ints[0] * list_of_ints[1]

        high_prod_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

        for i in list_of_ints[2:]:

            high_prod_3 = max(high_prod_3,i * high_prod_2,i * low_prod_2)

            high_prod_2 = max(high_prod_2,i * high,i * low)

            low_prod_2 = min(low_prod_2,i * high,i * low)

            high = max(high, i)

            low = min(low, i)

            # print(high_prod_3)

        return high_prod_3















# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)