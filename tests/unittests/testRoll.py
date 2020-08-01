#!/usr/bin/env python3

import unittest
import roll

class TestAnalytics(unittest.TestCase):

    def test_rollDice(self):
        self.assertEqual(roll.rollDice(10, 6).size, 10)
        self.assertLessEqual(max(roll.rollDice(1000, 6)), 6)
        self.assertGreaterEqual(min(roll.rollDice(1000, 6)), 1)

    def test_countSuccessfulRolls(self):
        self.assertEqual(roll.countSuccessfulRolls([6, 6, 6, 6, 6, 6], 4), 6)
        self.assertEqual(roll.countSuccessfulRolls([1, 1, 1, 1, 1, 1], 4), 0)
        self.assertEqual(roll.countSuccessfulRolls([6, 5, 4, 3, 2, 1], 4), 3)
        self.assertEqual(roll.countSuccessfulRolls([7, 7, 7, 7, 7, 7], 8), 0)



if __name__ == '__main__':
    unittest.main()