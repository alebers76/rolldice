import unittest
import io
import sys

from rolldice_functions import *

class TestDice(unittest.TestCase):
    """Test the functions in rolldice.py"""

    def setUp(self):
        """Initialize the dice tests."""
        self.test_dice = 4
        self.test_numrolls = 3
        self.test_rand_results = [1, 2, 3, 4]
        self.test_allrolls = [[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 1, 4], 
            [1, 2, 2], [1, 2, 3], [1, 2, 4], [1, 3, 3], [1, 3, 4], [1, 4, 4],
            [2, 2, 2], [2, 2, 3], [2, 2, 4], [2, 3, 3], [2, 3, 4], [2, 4, 4], 
            [3, 3, 3], [3, 3, 4], [3, 4, 4], [4, 4, 4]]
        self.test_matchingrolls = [[1, 3, 4], [2, 2, 4], [2, 3, 3]]

    def test_display_results(self):
        """Test the report_results function."""
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        report_results(len(self.test_allrolls), self.test_matchingrolls, 8)
        sys.stdout = sys.__stdout__                     # Reset redirect.
        self.assertEqual(capturedOutput.getvalue().strip(), "Out of 20 rolls, there are 3 possible rolls (15.0%) that sum to 8.")  

    def test_rolldie(self):
        """Test rolling a die."""
        test_roll = []
        for i in range(1, 50):
            test_roll.append(rolldie(self.test_dice))
        for i in range(50):
            self.assertIn(test_roll[i-1], self.test_rand_results)

    def test_rolldice(self):
        """Test rolling the dice."""
        test_results = rolldice(self.test_dice, self.test_numrolls)
        self.assertEqual(len(test_results['rolls']), self.test_numrolls)
        test_total = False
        if (test_results['total'] >= self.test_numrolls) and (test_results['total'] <= self.test_numrolls * self.test_dice):
            test_total = True
        self.assertTrue(test_total)

    def test_rollresults(self):
        """Test the user roll."""
        test_results = get_roll_results(self.test_dice, self.test_numrolls)
        test_total = False
        if (test_results >= self.test_numrolls) and (test_results <= self.test_numrolls * self.test_dice):
            test_total = True
        self.assertTrue(test_total)

unittest.main()
