__author__ = 'zephaniahgrunschlag'

"""
Google Code Jam, May 31 2014, Problem A.

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

from sortedcontainers import SortedList

class DataPacking(object):
    """
    Solver for Google Code Jam's May 31 2014, Problem A.
    """
    def __init__(self, the_input):
        """
        Initialize the solver. Just storing the input for the solve() method
        :param the_input: The challenge.
        :type the_input: str
        :return: self
        :rtype: DataPacking
        """
        self.the_input = the_input

    def solve(self):
        """
        According to flake8, this has a cyclomatic complexity of 9, close to the max recommended of 10
        (the flake8 command was: flake8 --max-complexity 3 code_jam_data_packing.py)
        According to radon, the cc is 8
        (the radon command was: radon cc code_jam_data_packing.py -a -s)
        Solve the problem
        :return: the solution
        :rtype: str
        """
        #unpack the input:
        lines = self.the_input.split("\n")
        T = int(lines[0]) #the number of challenges
        challenges = []
        for i in range(T):
            challenge_def_line = lines[2*i+1]
            filesizes_line = lines[2*i+2]
            N, S = map(int, challenge_def_line.split()) #number of files, and max file size
            challenges.append({"S": S, "N": N, "filesizes": map(int, filesizes_line.split())})

        """
        solve each challenge using a heuristic algorithm:
        Suppose we are trying to fill in our next disc.
        Pick the next available file (since it must be in SOME disc).
        Find the file that can be added to that disc and results in the least wasted space.
        Go on to the next disc, etc.
        """
        for challenge in challenges:
            S, N = challenge["S"], challenge["N"]
            sizes = SortedList(challenge["filesizes"])
            discs = []
            next_file_large = next_file_small = None
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
            challenge["solution"] = len(discs)

        #print the expected output in a string
        res = ""
        for i in range(T):
            res += "Case #{}: {}\n".format(i+1, challenges[i]["solution"])

        return res.strip()