#!/usr/bin/env python3

import unittest
import analytics

class TestAnalytics(unittest.TestCase):

    def test_averageOfRoll(self):
        self.assertEqual(analytics.averageOfRoll([1, 2, 3, 4, 5, 6]), 3.5)
        self.assertEqual(analytics.averageOfRoll([6, 5, 4, 3, 2, 1]), 3.5)
        self.assertEqual(analytics.averageOfRoll([1, 1, 1, 1, 1, 1]), 1)
        self.assertEqual(analytics.averageOfRoll([6, 6, 6, 6, 6, 6]), 6)
        self.assertEqual(analytics.averageOfRoll([6.1, 6.1, 6.1, 6.1, 6.1, 6.1]), 6.1) # Tests rounding errors

    def test_averageOfDice(self):
        self.assertEqual(analytics.averageOfDice(6), 3.5)
        self.assertEqual(analytics.averageOfDice(6.1), 3.55)
        self.assertEqual(analytics.averageOfDice(7), 4)
        self.assertEqual(analytics.averageOfDice(10), 5.5)
        self.assertEqual(analytics.averageOfDice(20), 10.5)

    def test_expectedCountSuccessfulRolls(self):
        self.assertEqual(analytics.expectedCountSuccessfulRolls(6, 10, 4), 5)
        self.assertEqual(analytics.expectedCountSuccessfulRolls(6, 100000, 4), 50000)
        self.assertEqual(analytics.expectedCountSuccessfulRolls(7, 10, 4), 5.7142857142857135)
        self.assertEqual(analytics.expectedCountSuccessfulRolls(6.1, 10.1, 4.1), 4.967213114754099) # This test case is dubious, the true number should be far lower as 4.1+ on a dice is equal to 5+
        self.assertEqual(analytics.expectedCountSuccessfulRolls(20, 10, 14), 3.5)


if __name__ == '__main__':
    unittest.main()