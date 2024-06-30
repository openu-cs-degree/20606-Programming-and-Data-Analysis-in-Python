"""
File: preparation.py
Author: Yehonatan Simian

+------------------------------------------------------------------------------------+
|         20606 - Programming and Data Analysis in Python - Exam Preparation         |
|                                                                                    |
|                 "One must imagine Sisyphus happy." - Albert Camus                  |
+------------------------------------------------------------------------------------+

This module contains the solutions to all 11 exam preparation problems, as well as
a solution to the 26/06/2024 exam.
All functions have been tested using the provided test cases in preparation.test.py.

Allowed functions:
   python: abs, float, input, int, isinstance, len, list,
           max, min, pow, print, range, sorted, str, sum, tuple
   str:    slicing, in, +
   list:   slicing, in, +, sort, pop, copy, append

Disclaimer:
I hereby declare that the solutions provided in this file are entirely my own.
These solutions are not official, thus I am not responsible for any use of these solutions.
In particular, and I might have mistakes in my solutions. If you find any, please let me know.
"""

# pylint: disable=consider-using-enumerate
# pylint: disable=redefined-builtin
# pylint: disable=too-few-public-methods
# pylint: disable=consider-using-generator
# pylint: disable=protected-access

# Prolouge: auxiliaries


def is_square(mat: list) -> bool:
    """Check if the matrix is square."""
    if len(mat) == 0:
        return False

    for row in mat:
        if len(row) != len(mat):
            return False

    return True


def index_of(num: int, lst: list) -> int:
    """Return the index of the number in the list."""
    if not lst:
        return -1
    if lst[0] == num:
        return 0
    index = index_of(num, lst[1:])
    if index != -1:
        index += 1
    return index


class Time:
    """A class representing time in hours and minutes."""

    def __init__(self, h: int = 0, m: int = 0) -> None:
        if not 0 <= h <= 23:
            h = 0
        if not 0 <= m <= 59:
            m = 0
        self._hour = h
        self._minute = m


# Problem 1: is_serpertine


def is_serpertine(mat: list) -> bool:
    """Check if the matrix is serpertine."""
    if not is_square(mat) or mat[0][0] != 1:
        return False

    n = len(mat)
    for i in range(n):
        for j in range(1, n):
            if i % 2 == 0:  # Check ascending order for even rows
                if not mat[i][j] - mat[i][j - 1] == 1:
                    return False
            else:  # Check descending order for odd rows
                if not mat[i][j - 1] - mat[i][j] == 1:
                    return False

    return True


# Problem 2: is_identity, max_matrix


def is_identity(mat: list, x: int, size: int) -> bool:
    """Check if the submatrix starting at (x, x) with the given size is an identity matrix."""
    if not is_square(mat) or x < 0 or x + size > len(mat) or size < 1:
        return False

    for i in range(size):
        for j in range(size):
            if (i == j and mat[x + i][x + j] != 1) or (
                i != j and mat[x + i][x + j] != 0
            ):
                return False

    return True


def max_matrix(mat: list) -> int:
    """Return the maximum size of an identity central submatrix."""
    # Note: we may assume that the matrix is square and of odd size

    n = len(mat)
    for x in range(n // 2 + 1):
        size = n - x * 2
        if is_identity(mat, x, size):
            return size

    return 0


# Problem 3: exist, find_pair
# Note: we may not use the built-in function `in`.
# Note: we may assume that the list's elements are distinct.


def exist(num: int, lst: list) -> bool:
    """Check if the number exists in the list."""
    if not lst:
        return False
    return lst[0] == num or exist(num, lst[1:])


def find_pair(sum: int, lst: list) -> bool:
    """Check if there are two numbers in the list that sum up to the given number."""
    if not lst:
        return False
    return exist(sum - lst[0], lst[1:]) or find_pair(sum, lst[1:])


# Problem 4: minus_plus


def minus_plus(lst: list) -> bool:
    """Check if each element has a negative twin."""
    if len(lst) % 2 != 0:
        return False

    def helper(sublist: list) -> bool:
        if not sublist:
            return True
        return exist(-sublist[0], lst) and helper(sublist[1:])

    return helper(lst)


# problem 5: max_mul2


def max_mul2(lst: list) -> int:
    """Find the largest possible product of two elements in a list"""
    max1 = max2 = float("-inf")
    min1 = min2 = float("inf")

    for num in lst:
        # Update the two largest values
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

        # Update the two smallest values
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    return max(max1 * max2, min1 * min2)


# problem 6: secret


def secret(s1: str, s2: str, key: int) -> bool:
    """Determines if the second string is derived from the first string using the key."""
    if len(s1) != len(s2):
        return False

    def helper(index: int) -> bool:
        if index == len(s1):
            return True
        if ord(s1[index]) + key + index != ord(s2[index]):
            return False
        return helper(index + 1)

    return helper(0)


# problem 7: bulls_and_cows


def bulls_and_cows(number: list, guess: list) -> int:
    """Calculate the number of bulls and cows in a guess."""

    def helper(number: list, guess: list, guess_index: int) -> int:
        if guess_index >= len(guess):
            return 0
        number_index = index_of(guess[guess_index], number)
        points = 0
        if number_index != -1:
            points += 1
        if number_index == guess_index:
            points += 1
        return points + helper(number, guess, guess_index + 1)

    return helper(number, guess, 0)


# problem 8: print_pairs


def print_pairs(arr: list, k: int) -> None:
    """Print all pairs in the list whose difference is exactly k."""
    n = len(arr)
    if n < 2:
        return
    left, right = 0, 1
    while right < n:
        diff = arr[right] - arr[left]
        if diff == k:
            print(f"({arr[left]}, {arr[right]})")
            left += 1
            right += 1
        elif diff > k:
            left += 1
            if left == right:
                right += 1
        else:
            right += 1


# problem 9: maximal_drop


def maximal_drop(lst: list) -> int:
    """Calculate the maximal drop between two heights in a list."""
    if not lst:
        return 0

    max_drop = 0
    max_height_so_far = lst[0]

    for height in lst:
        if height > max_height_so_far:
            max_height_so_far = height
        else:
            drop = max_height_so_far - height
            if drop > max_drop:
                max_drop = drop

    return max_drop


# problem 10: coffee shop


class Date:
    """A class representing dates (very poorly)."""

    def __init__(self, d: int, m: int, y: int) -> None:
        self._day = d
        self._month = m
        self._year = y

    # problem 10 section a
    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Date)
            and self._year == other._year
            and self._month == other._month
            and self._day == other._day
        )

    # problem 11 section a
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Date):
            return False
        if self._year != other._year:
            return self._year < other._year
        if self._month != other._month:
            return self._month < other._month
        return self._day < other._day


class Order:
    """A class representing an order in a coffee shop."""

    _order_num = 1

    # pylint: disable=too-many-arguments
    # problem 10 section b
    def __init__(self, day, month, year, hour, minute, cost=50) -> None:
        self._t = Time(hour, minute)
        self._d = Date(day, month, year)
        self._cost = cost
        self._order_id = Order._order_num
        Order._order_num += 1

    # problem 10 section c
    def __gt__(self, other: object) -> bool:
        return isinstance(other, Order) and self._cost > other._cost


class CashRegister:
    """A class representing a cash register in a coffee shop."""

    def __init__(self) -> None:
        self._orders = []

    # problem 10 section d
    def monthly_total_income(self, month: int) -> int:
        """Calculate the total income of a given month."""
        return sum([order._cost for order in self._orders if order._d._month == month])

    # problem 10 section e
    def most_expensive_order(self, date: Date) -> int:
        """Find the most expensive order on a given date."""
        return max([order for order in self._orders if order._d == date])._order_id

    # problem 10 section f
    def less_than(self, cost) -> list | None:
        """Return all orders with a cost less than a given value."""
        filtered_orders = [order for order in self._orders if order._cost < cost]
        return filtered_orders if filtered_orders else None


# problem 11: humans (now THAT'S a real problem)


class Person:
    """A class representing a person."""

    # problem 11 section b
    def __init__(self, name: str, id: int, birth: Date) -> None:
        self._name = name
        self._id = id
        self._birth = birth

    # problem 11 section c
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Person) and self._id == other._id


class ContactsList:
    """A class representing a list of contacts."""

    def __init__(self) -> None:
        self._contacts = []

    # problem 11 section d
    def born_in_date(self, d: Date) -> list:
        """Return all contacts born on a given date."""
        return [contact for contact in self._contacts if contact._birth == d]

    # problem 11 section e
    def oldest_contact(self) -> Person:
        """Return the oldest contact in the list."""

        def get_birth(contact: Person) -> Date:
            return contact._birth

        return min(self._contacts, key=get_birth)

    # problem 11 section f
    def born_in_month(self) -> list:
        """Return a list of tuples of the form (month, number of contacts born in that month)."""
        months = [0] * 13
        for contact in self._contacts:
            months[contact._birth._month] += 1
        return [(i, months[i]) for i in range(1, 13)]


# exam questions 26/06/2024


# q1a, assume the list has at least 2 zeroes
def biggest_sum(lst):
    """Return the biggest sum of integers between 2 zeroes in the list."""
    max_sum = 0
    curr_sum = 0

    for num in lst[index_of(0, lst) + 1 :]:
        if num == 0:
            max_sum = max(max_sum, curr_sum)
            curr_sum = 0
        else:
            curr_sum += num

    return max_sum


# q1b
def biggest_sum_row(mat):
    """Return the index of the row with the biggest sum of integers between 2 zeroes."""
    if not mat:
        return None

    max_sum = 0
    max_index = 0

    for i in range(len(mat)):
        curr_sum = biggest_sum(mat[i])
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_index = i

    return max_index


# q2
def common(lst1, lst2):
    """Return the common elements of both lists. If there are no such - it returns None."""
    commons_lst = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] == lst2[j]:
            commons_lst.append(lst1[i])
            i += 1
            j += 1
        elif lst1[i] > lst2[j]:
            j += 1
        else:
            i += 1

    return commons_lst or None


# q3a
def max_pos_seq(lst):
    """Return the number of highest sequence of consecutive positive numbers in the list."""

    def helper(lst, curr_seq):
        if not lst:
            return curr_seq
        if lst[0] <= 0:
            return max(curr_seq, helper(lst[1:], 0))
        return helper(lst[1:], curr_seq + 1)

    return helper(lst, 0)


# q3b
def is_palindrome(lst):
    """Return whether all elements, as well as the list itself, are palindromes."""
    if not lst:
        return True

    begin, end = lst[0], lst[-1]

    return begin == end == begin[::-1] and is_palindrome(lst[1:-1])


# q4 is boring


# q5 (Note: I'm not sure that this solution is the best one)
def mirror_list(mat):
    """Check if the matrix is a mirror list."""
    if not mat or not mat[0]:
        return False

    def check_equality_2(el1, el2):
        if not isinstance(el1, str) or not isinstance(el2, str):
            raise TypeError("The matrix must contain only strings")
        if len(el1) != 1 or len(el2) != 1:
            raise ValueError("The matrix must contain only single characters")
        return el1 == el2

    def check_equality_4(el1, el2, el3, el4):
        return check_equality_2(el1, el2) and check_equality_2(el3, el4) and el2 == el3

    mid_x = len(mat) // 2
    mid_y = len(mat[0]) // 2
    for i in range(mid_x):
        for j in range(mid_y):
            if not check_equality_4(mat[i][j], mat[i][~j], mat[~i][j], mat[~i][~j]):
                return False

    if len(mat) % 2 == 1:
        for i in range(mid_x + 1):
            if not check_equality_2(mat[mid_x][i], mat[mid_x][~i]):
                return False

    if len(mat[0]) % 2 == 1:
        for j in range(mid_y + 1):
            if not check_equality_2(mat[j][mid_y], mat[~j][mid_y]):
                return False

    return True


# epilogue: Yoni HaMelech
