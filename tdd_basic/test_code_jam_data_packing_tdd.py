__author__ = 'zephaniahgrunschlag'

"""
According to flake8, this class has a worst case MUCH IMPROVED
cyclomatic complexity of 6 (versus 9 previously)
(the flake8 command was: flake8 --max-complexity 3 code_jam_data_packing.py)
According to radon, the cc is a MUCH IMPROVED 2.0 (A grade).
The worst it gets is the solve_challenge() method with a cc of 5 (versus 8 before).
(the radon command was: radon cc code_jam_data_packing_tdd.py -a -s)
Solve the problem

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
from code_jam_data_packing_tdd import DataPacking

class DataPackingTest(TestCase):
    def setUp(self):
        self.input_str = """3
3 100
10 20 70
4 100
30 40 60 70
5 100
10 20 30 40 60"""
        self.challenge1 = """3 100
10 20 70"""
        self.challenge2 = """4 100
30 40 60 70"""
        self.challenge3 = """5 100
10 20 30 40 60"""
        self.expected_parse = {
            "T": 3,
            "challenges": [
                {"N": 3, "S": 100, "filesizes": [10, 20, 70]},
                {"N": 4, "S": 100, "filesizes": [30, 40, 60, 70]},
                {"N": 5, "S": 100, "filesizes": [10, 20, 30, 40, 60]}
            ]
        }
        self.parsed1 = self.expected_parse["challenges"][0]
        self.parsed2 = self.expected_parse["challenges"][1]
        self.parsed3 = self.expected_parse["challenges"][2]

        self.expected_disc_lens = [2, 2, 3]
        self.expected_disc_len1 = self.expected_disc_lens[0]
        self.expected_disc_len2 = self.expected_disc_lens[1]
        self.expected_disc_len3 = self.expected_disc_lens[2]

        self.expected_solution = """Case #1: 2
Case #2: 2
Case #3: 3"""
        self.data_packer = DataPacking(self.input_str)

    def test_init(self):
        self.assertEquals(self.input_str, self.data_packer.input_str)
        self.assertIsNone(self.data_packer.T)
        self.assertIsNone(self.data_packer.challenges)
        self.assertIsNone(self.data_packer.disc_lens)
        self.assertIsNone(self.data_packer.solution)

    def test_parse_challenge(self):
        self.assertDictEqual(self.parsed1, self.data_packer.parse_challenge(self.challenge1))
        self.assertDictEqual(self.parsed2, self.data_packer.parse_challenge(self.challenge2))
        self.assertDictEqual(self.parsed3, self.data_packer.parse_challenge(self.challenge3))

    def test_parse_input(self):
        self.assertDictEqual(self.expected_parse, self.data_packer.parse_input())
        self.assertEqual(self.expected_parse["T"], self.data_packer.T)
        self.assertListEqual(self.expected_parse["challenges"], self.data_packer.challenges)

    def test_solve_challenge(self):
        self.assertEquals(self.expected_disc_len1, self.data_packer.solve_challenge(self.parsed1))
        self.assertEquals(self.expected_disc_len2, self.data_packer.solve_challenge(self.parsed2))
        self.assertEquals(self.expected_disc_len3, self.data_packer.solve_challenge(self.parsed3))

    def test_solve_discs(self):
        self.data_packer.T = self.expected_parse["T"]
        self.data_packer.challenges = self.expected_parse["challenges"]
        self.assertListEqual(self.expected_disc_lens, self.data_packer.solve_discs())
        self.assertListEqual(self.expected_disc_lens, self.data_packer.disc_lens)

    def test_format_output(self):
        self.assertEquals(self.expected_solution, self.data_packer.format_output(self.expected_disc_lens))

    def test_solve(self):
        self.assertEquals(self.expected_solution, self.data_packer.solve())
        self.assertEquals(self.expected_solution, self.data_packer.solution)
