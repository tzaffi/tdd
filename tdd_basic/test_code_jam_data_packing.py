__author__ = 'zephaniahgrunschlag'

"""
SEE: https://code.google.com/codejam/contest/3014486/dashboard

Input:
3
3 100
10 20 70
4 100
30 40 60 70
5 100
10 20 30 40 60

Output:
Case #1: 2
Case #2: 2
Case #3: 3
"""

from unittest.case import TestCase
from code_jam_data_packing import DataPacking

class DataPackingTest(TestCase):
    def test_solution(self):
        input = """3
3 100
10 20 70
4 100
30 40 60 70
5 100
10 20 30 40 60"""

        correct_output = """Case #1: 2
Case #2: 2
Case #3: 3"""

        dp = DataPacking(input)
        self.assertEquals(correct_output, dp.solve())
