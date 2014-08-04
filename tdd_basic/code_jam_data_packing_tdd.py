__author__ = 'zephaniahgrunschlag'

"""
Google Code Jam, May 31 2014, Problem A.

SEE: https://code.google.com/codejam/contest/3014486/dashboard

Test Driven Development example
"""
import copy
from sortedcontainers import SortedList


class DataPacking(object):
    """
    Solver for Google Code Jam's May 31 2014, Problem A.
    """
    def __init__(self, the_input):
        """
        Constructor. Saves input for later processing. Initialize members.
        :param the_input: Code Jam problem input string
        :type the_input: str
        :return: self
        :rtype: DataPacking
        """
        self.input_str = the_input
        self.T = self.challenges = self.disc_lens = self.solution = None

    @staticmethod
    def parse_challenge(challenge_str):
        """
        Parse a challenge string. Cull out N - the number of files,
        and S - the disc capacity
        :param challenge_str:
        1st line: N S
        2nd line: the N file sizes (all no greater than S)
        :type challenge_str: str
        :return: A dict with keys N, S, and filesizes and appropriate values
        :rtype: dict
        """
        challenge_def_line, filesizes_line = challenge_str.split("\n")
        N, S = map(int, challenge_def_line.split())  # number of files, and max file size
        challenge = {"S": S, "N": N, "filesizes": map(int, filesizes_line.split())}
        return challenge

    def parse_input(self):
        """
        Parse all the input in self.input_str. Save the parsed data
        to self.T and self.challenges
        :return: dict with keys T and challenges
        :rtype: dict
        """
        lines = self.input_str.split("\n")
        self.T = int(lines[0]) #the number of challenges
        self.challenges = []
        for i in range(self.T):
            j = 2*i + 1
            challenge_str = lines[j] + "\n" + lines[j+1]
            self.challenges.append(self.parse_challenge(challenge_str))
        return {"T": self.T, "challenges": copy.deepcopy(self.challenges)}

    @staticmethod
    def solve_challenge(challenge):
        """
        Solve a challenge using a greedy algorithm.
        Suppose we are trying to fill in our next disc.
        Pick the next available file (since it must be in SOME disc).
        Find the file that can be added to that disc and results in the least wasted space.
        Go on to the next disc, etc.
        ASSUMPTION: self.parse_input() has been previously called
        :param challenge: A dict with keys N, S, and filesizes and appropriate values
        :type challenge: dict
        :return: number of discs needed
        :rtype: int
        """
        S, N = challenge["S"], challenge["N"]
        sizes = SortedList(challenge["filesizes"])
        discs = []
        while sizes:
            next_file_large = sizes.pop()
            found_a_good_fit = False
            for next_file_small in reversed(sizes):
                if next_file_large + next_file_small <= S:
                    found_a_good_fit = True
                    break
            if found_a_good_fit:
                discs.append((next_file_large, next_file_small))
                sizes.remove(next_file_small)
            else:
                discs.append((next_file_large,))
        return len(discs)

    def solve_discs(self):
        """
        Solve all the challenges. Save the results in self.dics_lens.
        ASSUMPTION: self.parse_input() and self.parse_input() have
        been previously called in order.
        :return: self.disc_lens
        :rtype: list
        """
        self.disc_lens = []
        for challenge in self.challenges:
            self.disc_lens.append(self.solve_challenge(challenge))
        return self.disc_lens

    @staticmethod
    def format_output(disc_lens):
        """
        Create a string of the expected format. Eg:
        'Case #1: 2\nCase #2: 2\nCase #3: 3'
        :param disc_lens: The disc lengths
        :type disc_lens: list
        :return: Properly formatted string
        :rtype: str
        """
        res = ""
        for i in range(len(disc_lens)):
            res += "Case #{}: {}\n".format(i+1, disc_lens[i])
        return res.strip()

    def solve(self):
        """
        Run the entire algorithm from end to end, including:
        parsing the input, solving the problem, and formatting the result.
        Save the result in self.solution as well.
        :return: formattted output
        :rtype: str
        """
        self.parse_input()
        self.solve_discs()
        self.solution = self.format_output(self.disc_lens)
        return self.solution
