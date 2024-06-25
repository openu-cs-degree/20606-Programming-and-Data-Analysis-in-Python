"""
File: preparation.test.py
Author: Yehonatan Simian

This module contains unit tests for the preparation module.
"""

# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=protected-access
# pylint: disable=wildcard-import

import sys
import unittest
from io import StringIO
from preparation import *


class TestIsSquare(unittest.TestCase):
    def test_empty_matrix(self):
        """Test that an empty matrix returns False."""
        self.assertFalse(is_square([]))

    def test_non_square_matrix_more_rows(self):
        """Test that a matrix with more rows than columns returns False."""
        mat = [[1, 2], [3, 4], [5, 6]]
        self.assertFalse(is_square(mat))

    def test_non_square_matrix_more_columns(self):
        """Test that a matrix with more columns than rows returns False."""
        mat = [[1, 2, 3], [4, 5, 6]]
        self.assertFalse(is_square(mat))

    def test_square_matrix(self):
        """Test that a square matrix returns True."""
        mat = [[1, 2], [3, 4]]
        self.assertTrue(is_square(mat))

    def test_single_element_matrix(self):
        """Test that a matrix with a single element returns True."""
        mat = [[1]]
        self.assertTrue(is_square(mat))


class TestIsSerpertine(unittest.TestCase):
    def test_serpertine_true(self):
        self.assertTrue(is_serpertine([[1, 2, 3], [6, 5, 4], [7, 8, 9]]))

    def test_serpertine_false(self):
        self.assertFalse(is_serpertine([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        self.assertFalse(is_serpertine([[1, 3, 3], [6, 5, 4], [7, 8, 9]]))

    def test_serpertine_false_even_row_not_ascending(self):
        self.assertFalse(is_serpertine([[1, 3, 2], [6, 5, 4], [7, 8, 9]]))

    def test_serpertine_false_odd_row_not_descending(self):
        self.assertFalse(is_serpertine([[1, 2, 3], [6, 4, 5], [7, 8, 9]]))

    def test_empty_matrix(self):
        self.assertFalse(is_serpertine([]))

    def test_single_row_matrix(self):
        self.assertFalse(is_serpertine([[1, 2, 3]]))

    def test_varying_length_rows(self):
        self.assertFalse(is_serpertine([[1, 2], [5, 4, 3], [6, 7, 8]]))

    def test_single_element_matrix(self):
        self.assertTrue(is_serpertine([[1]]))

    def test_single_element_matrix_false(self):
        self.assertFalse(is_serpertine([[2]]))

    def test_2x2_matrix_true(self):
        self.assertTrue(is_serpertine([[1, 2], [4, 3]]))

    def test_2x2_matrix_false(self):
        self.assertFalse(is_serpertine([[1, 2], [3, 4]]))
        self.assertFalse(is_serpertine([[1, 2], [4, 4]]))


class TestIsIdentity(unittest.TestCase):
    def test_empty_matrix(self):
        self.assertFalse(is_identity([], 0, 0))

    def test_non_square_matrix(self):
        mat = [[1, 0], [0, 1], [1, 0]]
        self.assertFalse(is_identity(mat, 0, 2))

    def test_valid_identity_matrix(self):
        mat = [[1, 0], [0, 1]]
        self.assertTrue(is_identity(mat, 0, 2))

    def test_invalid_identity_correct_diagonals(self):
        mat = [[1, 0, 0], [0, 1, 0], [1, 0, 1]]
        self.assertFalse(is_identity(mat, 0, 3))

    def test_submatrix_as_identity(self):
        mat = [[2, 2, 2, 2], [2, 1, 0, 0], [2, 0, 1, 0], [2, 0, 0, 1]]
        self.assertTrue(is_identity(mat, 1, 3))

    def test_out_of_bounds(self):
        mat = [[1, 0], [0, 1]]
        self.assertFalse(is_identity(mat, 1, 2))

    def test_negative_start_index(self):
        mat = [[1, 0], [0, 1]]
        self.assertFalse(is_identity(mat, -1, 2))

    def test_size_zero(self):
        mat = [[1, 0], [0, 1]]
        self.assertFalse(is_identity(mat, 0, 0))


class TestMaxMatrix(unittest.TestCase):
    def test_single_element_matrix(self):
        self.assertEqual(max_matrix([[1]]), 1)
        self.assertEqual(max_matrix([[0]]), 0)

    def test_square_matrix_without_identity_submatrix(self):
        self.assertEqual(max_matrix([[1, 0, 1], [0, 1, 0], [0, 0, 1]]), 1)

    def test_square_matrix_with_full_identity(self):
        self.assertEqual(max_matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 3)

    def test_square_matrix_with_partial_identity_submatrix(self):
        self.assertEqual(max_matrix([[1, 0, 3], [0, 1, 4], [5, 6, 1]]), 1)
        self.assertEqual(max_matrix([[1, 0, 0], [0, 0, 0], [0, 0, 1]]), 0)

    def test_square_matrix_with_multiple_identity_submatrices(self):
        self.assertEqual(
            max_matrix(
                [
                    [1, 0, 0, 0, 0, 0, 2],
                    [0, 1, 0, 0, 0, 0, 2],
                    [0, 0, 1, 0, 0, 0, 3],
                    [0, 0, 0, 1, 0, 0, 4],
                    [0, 0, 0, 0, 1, 0, 5],
                    [0, 0, 0, 0, 0, 1, 5],
                    [6, 6, 7, 8, 9, 9, 10],
                ]
            ),
            5,
        )

    def test_staff_matrix(self):
        self.assertEqual(
            max_matrix(
                [
                    [1, 2, 3, 2, 0, 1, 2],
                    [0, 1, 0, 0, 0, 3, 0],
                    [0, 0, 1, 0, 0, 0, 0],
                    [5, 0, 0, 1, 0, 0, 0],
                    [7, 0, 0, 0, 1, 0, 0],
                    [8, 0, 0, 0, 0, 1, 0],
                    [1, 0, 0, 0, 0, 0, 0],
                ]
            ),
            3,
        )


class TestExistFunction(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(exist(1, []), "Should return False for empty list")

    def test_single_element_list_found(self):
        self.assertTrue(
            exist(1, [1]),
            "Should return True for single element list when element is found",
        )

    def test_single_element_list_not_found(self):
        self.assertFalse(
            exist(1, [2]),
            "Should return False for single element list when element is not found",
        )

    def test_multiple_elements_list_found(self):
        self.assertTrue(
            exist(1, [0, 1, 2]),
            "Should return True when element is in the middle of the list",
        )
        self.assertTrue(
            exist(1, [1, 2, 3]),
            "Should return True when element is at the beginning of the list",
        )
        self.assertTrue(
            exist(1, [2, 3, 1]),
            "Should return True when element is at the end of the list",
        )

    def test_multiple_elements_list_not_found(self):
        self.assertFalse(
            exist(1, [2, 3, 4]), "Should return False when element is not in the list"
        )

    def test_negative_numbers(self):
        self.assertTrue(
            exist(-1, [-1, 0, 1]),
            "Should return True for negative numbers when element is found",
        )
        self.assertFalse(
            exist(-1, [1, 2, 3]),
            "Should return False for negative numbers when element is not found",
        )

    def test_zero(self):
        self.assertTrue(
            exist(0, [0, 1, 2]),
            "Should return True when looking for 0 and it is in the list",
        )
        self.assertFalse(
            exist(0, [1, 2, 3]),
            "Should return False when looking for 0 and it is not in the list",
        )


class TestFindPair(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(find_pair(5, []))

    def test_single_element(self):
        self.assertFalse(find_pair(5, [5]))

    def test_no_pair_found(self):
        self.assertFalse(find_pair(10, [1, 2, 3, 4, 5]))

    def test_pair_found(self):
        self.assertTrue(find_pair(5, [1, 2, 3, 4]))

    def test_negative_numbers(self):
        self.assertTrue(find_pair(-1, [-5, 4, -1, 0]))

    def test_zero_sum(self):
        self.assertTrue(find_pair(0, [-1, 1, 2, 3]))

    def test_large_list(self):
        large_list = list(range(100))
        self.assertTrue(find_pair(197, large_list))


class TestMinusPlus(unittest.TestCase):
    def test_even_length_with_twins(self):
        self.assertTrue(minus_plus([1, -1, 2, -2]))
        self.assertTrue(minus_plus([-3, 3, 4, -4, 5, -5]))

    def test_odd_length(self):
        self.assertFalse(minus_plus([1, -1, 2]))
        self.assertFalse(minus_plus([-3, 3, 4, -4, 5]))

    def test_even_length_without_twins(self):
        self.assertFalse(minus_plus([1, 2, 3, 4]))
        self.assertFalse(minus_plus([-1, -2, -3, -4]))

    def test_empty_list(self):
        self.assertTrue(minus_plus([]))

    def test_single_pair(self):
        self.assertTrue(minus_plus([1, -1]))
        self.assertTrue(minus_plus([-2, 2]))

    def test_no_twins(self):
        self.assertFalse(minus_plus([1, 2, 3, -1, -2, -4]))


class TestMatMul2(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(max_mul2([1, 2]) == 2)
        self.assertTrue(max_mul2([-1, -2]) == 2)
        self.assertTrue(max_mul2([1, -2]) == -2)

    def test_large(self):
        self.assertTrue(max_mul2([1, 2, 3, 4, 5]) == 20)
        self.assertTrue(max_mul2([-1, -2, -3, -4, -5]) == 20)
        self.assertTrue(max_mul2([-10, -20, 1, 2, 3]) == 200)

    def test_identicals(self):
        self.assertTrue(max_mul2([5, 5, 5, 5, 5]) == 25)

    def test_spread(self):
        self.assertTrue(max_mul2([-1, 2, -3]) == 3)
        self.assertTrue(max_mul2([-1, 2, -3, 4]) == 8)
        self.assertTrue(max_mul2([1, -2, 3, -4, 5]) == 15)


class TestSecretFunction(unittest.TestCase):
    def test_basic(self):
        self.assertTrue(secret("aaa", "bcd", 1))
        self.assertFalse(secret("aaa", "bce", 1))

    def test_different_lengths(self):
        self.assertFalse(secret("aaa", "cdef", 2))
        self.assertFalse(secret("a", "", 1))

    def test_empty_strings(self):
        self.assertTrue(secret("", "", 2))

    def test_single_character(self):
        self.assertTrue(secret("a", "c", 2))
        self.assertFalse(secret("a", "d", 2))

    def test_large_key(self):
        self.assertTrue(secret("abc", "egi", 4))


class TestPrintPairs(unittest.TestCase):
    def _assert_output(self, arr, k, expected):
        captured_output = StringIO()
        sys.stdout = captured_output
        print_pairs(arr, k)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected)

    def test_staff(self):
        arr = [-7, -3, 0, 1, 3, 5, 12, 14, 17, 19, 25, 30]
        self._assert_output(arr, 2, "(1, 3)\n(3, 5)\n(12, 14)\n(17, 19)\n")
        self._assert_output(arr, 6, "(-3, 3)\n(19, 25)\n")
        self._assert_output(arr, 23, "")

    def test_simple(self):
        arr = [1, 3, 5, 7, 9]

        self._assert_output(arr, 1, "")
        self._assert_output(arr, 2, "(1, 3)\n(3, 5)\n(5, 7)\n(7, 9)\n")
        self._assert_output(arr, 3, "")
        self._assert_output(arr, 4, "(1, 5)\n(3, 7)\n(5, 9)\n")
        self._assert_output(arr, 5, "")
        self._assert_output(arr, 6, "(1, 7)\n(3, 9)\n")
        self._assert_output(arr, 7, "")
        self._assert_output(arr, 8, "(1, 9)\n")
        self._assert_output(arr, 9, "")
        self._assert_output(arr, 10, "")

    def test_single_element(self):
        arr = [1]

        self._assert_output(arr, 1, "")
        self._assert_output(arr, 2, "")
        self._assert_output(arr, 3, "")


class TestMaximalDrop(unittest.TestCase):
    def test_staff(self):
        self.assertEqual(maximal_drop([4, 6, 7, 24, 12, 27, 3, 21, 5]), 24)
        self.assertEqual(maximal_drop([14, 26, 7, 12, 22, 3, 21, 5]), 23)
        self.assertEqual(maximal_drop([14, 27, 7, 12, 22, 3, 15, 5]), 24)

    def test_empty_list(self):
        self.assertEqual(maximal_drop([]), 0)

    def test_single_element(self):
        self.assertEqual(maximal_drop([5]), 0)

    def test_no_drop(self):
        self.assertEqual(maximal_drop([5, 5, 5, 5]), 0)

    def test_simple(self):
        self.assertEqual(maximal_drop([5, 3, 6, 7, 4]), 3)
        self.assertEqual(maximal_drop([10, 2, 8, 1, 7]), 9)

    def test_decreasing_heights(self):
        self.assertEqual(maximal_drop([10, 9, 8, 7, 6]), 4)

    def test_increasing_heights(self):
        self.assertEqual(maximal_drop([1, 2, 3, 4, 5]), 0)


class TestDate(unittest.TestCase):
    def test_initialization(self):
        date = Date(15, 4, 2023)
        self.assertEqual(date._day, 15)
        self.assertEqual(date._month, 4)
        self.assertEqual(date._year, 2023)

    def test_eq(self):
        date1 = Date(15, 4, 2023)
        date2 = Date(15, 4, 2023)
        date3 = Date(16, 4, 2023)
        self.assertTrue(date1 == date2)
        self.assertFalse(date1 == date3)

    def test_lt(self):
        date1 = Date(15, 4, 2023)
        date2 = Date(16, 4, 2023)
        date3 = Date(15, 5, 2023)
        date4 = Date(15, 4, 2024)
        date5 = Date(15, 4, 2023)
        not_date = "15-04-2023"
        self.assertTrue(date1 < date2)
        self.assertTrue(date1 < date3)
        self.assertTrue(date1 < date4)
        self.assertFalse(date2 < date1)
        self.assertFalse(date1 < date5)
        self.assertFalse(date1 < not_date)


class TestOrder(unittest.TestCase):
    def tests(self):
        """All tests in one function to avoid order dependency."""
        order = Order(1, 1, 2023, 12, 30)
        self.assertEqual(order._t.__dict__, Time(12, 30).__dict__)
        self.assertEqual(order._d.__dict__, Date(1, 1, 2023).__dict__)
        self.assertEqual(order._cost, 50)
        self.assertEqual(order._order_id, 1)

        first_order = Order(1, 1, 2023, 12, 30, 100)
        second_order = Order(2, 1, 2023, 1, 15, 50)
        self.assertEqual(first_order._order_id + 1, second_order._order_id)
        self.assertEqual(first_order._order_id, 2)
        self.assertEqual(second_order._order_id, 3)

        cheaper_order = Order(1, 1, 2023, 12, 30, 50)
        expensive_order = Order(2, 1, 2023, 1, 15, 100)
        self.assertTrue(expensive_order > cheaper_order)
        self.assertFalse(cheaper_order > expensive_order)
        self.assertEqual(cheaper_order._order_id, 4)
        self.assertEqual(expensive_order._order_id, 5)

    def tearDown(self):
        Order._order_num = 1


class TestCashRegister(unittest.TestCase):
    def setUp(self):
        self.cash_register = CashRegister()

    def test_initialization(self):
        self.assertEqual(len(self.cash_register._orders), 0)

    def test_monthly_total_income(self):
        self.assertEqual(self.cash_register.monthly_total_income(1), 0)
        self.cash_register._orders.append(Order(1, 1, 2023, 10, 30, 50))
        self.cash_register._orders.append(Order(2, 1, 2023, 11, 30, 100))
        self.cash_register._orders.append(Order(2, 2, 2023, 11, 30, 100))
        self.assertEqual(self.cash_register.monthly_total_income(1), 150)
        self.assertEqual(self.cash_register.monthly_total_income(2), 100)
        self.assertEqual(self.cash_register.monthly_total_income(3), 0)

    def test_most_expensive_order(self):
        date = Date(1, 1, 2023)
        self.assertRaises(ValueError, self.cash_register.most_expensive_order, date)
        self.cash_register._orders.append(Order(1, 1, 2023, 10, 30, 50))
        self.cash_register._orders.append(Order(1, 1, 2023, 11, 30, 100))
        self.cash_register._orders.append(Order(1, 1, 2023, 11, 30, 70))
        self.cash_register._orders.append(Order(2, 2, 2023, 11, 30, 170))
        self.assertEqual(self.cash_register.most_expensive_order(date), 2)

    def test_less_than(self):
        self.assertIsNone(self.cash_register.less_than(50))
        self.cash_register._orders.append(Order(1, 1, 2023, 10, 30, 30))
        self.cash_register._orders.append(Order(2, 1, 2023, 11, 30, 70))
        self.assertEqual(len(self.cash_register.less_than(50)), 1)
        self.assertIsNone(self.cash_register.less_than(10))

    def tearDown(self):
        Order._order_num = 1


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.birth_date = Date(1, 1, 1990)
        self.person1 = Person("John Doe", 12345, self.birth_date)
        self.person2 = Person("Jane Doe", 12345, self.birth_date)
        self.person3 = Person("Jake Doe", 67890, self.birth_date)

    def test_initialization(self):
        self.assertEqual(self.person1._name, "John Doe")
        self.assertEqual(self.person1._id, 12345)
        self.assertEqual(self.person1._birth, self.birth_date)

    def test_equality_same_id(self):
        self.assertTrue(self.person1 == self.person2)

    def test_equality_different_id(self):
        self.assertFalse(self.person1 == self.person3)

    def test_equality_non_person_object(self):
        self.assertFalse(self.person1 == "NotAPerson")


class TestContactsList(unittest.TestCase):
    def setUp(self):
        self.contacts_list = ContactsList()
        self.date1 = Date(1, 1, 2000)
        self.date2 = Date(2, 2, 1990)
        self.date3 = Date(1, 1, 2000)
        self.person1 = Person("Alice", 1, self.date1)
        self.person2 = Person("Bob", 2, self.date2)
        self.person3 = Person("Charlie", 3, self.date3)

    def test_born_in_date_no_contacts(self):
        self.assertEqual(self.contacts_list.born_in_date(self.date1), [])

    def test_born_in_date_one_contact(self):
        self.contacts_list._contacts.append(self.person1)
        self.assertEqual(self.contacts_list.born_in_date(self.date1), [self.person1])

    def test_born_in_date_multiple_contacts(self):
        self.contacts_list._contacts.extend([self.person1, self.person2, self.person3])
        self.assertEqual(
            self.contacts_list.born_in_date(self.date1), [self.person1, self.person3]
        )

    def test_oldest_contact_no_contacts(self):
        with self.assertRaises(ValueError):
            self.contacts_list.oldest_contact()

    def test_oldest_contact_one_contact(self):
        self.contacts_list._contacts.append(self.person1)
        self.assertEqual(self.contacts_list.oldest_contact(), self.person1)

    def test_oldest_contact_multiple_contacts(self):
        self.contacts_list._contacts.extend([self.person1, self.person2, self.person3])
        self.assertEqual(self.contacts_list.oldest_contact(), self.person2)

    def test_born_in_month_no_contacts(self):
        self.assertEqual(
            self.contacts_list.born_in_month(), [(i, 0) for i in range(1, 13)]
        )

    def test_born_in_month_different_months(self):
        self.contacts_list._contacts.extend([self.person1, self.person2])
        expected = [(1, 1), (2, 1)] + [(i, 0) for i in range(3, 13)]
        self.assertEqual(self.contacts_list.born_in_month(), expected)

    def test_born_in_month_same_month(self):
        self.contacts_list._contacts.extend([self.person1, self.person3])
        expected = [(1, 2)] + [(i, 0) for i in range(2, 13)]
        self.assertEqual(self.contacts_list.born_in_month(), expected)


if __name__ == "__main__":
    unittest.main()
