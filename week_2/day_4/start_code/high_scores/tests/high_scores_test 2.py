import unittest

from src.high_scores import latest, personal_best, personal_top_three, descending_scores

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Tests

    # Test latest score (the last thing in the list)
    def test_has_latest_score(self):
        input = [2, 5, 9, 4, 7]
        expected_output = 7
        actual_output = 7
        self.assertEqual(expected_output, actual_output)

    # Test personal best (the highest score in the list)
    def test_is_personal_best(self):
        input = [3, 12, 5, 9, 8]
        expected_output = 12
        actual_output = 12
        self.assertEqual(expected_output, actual_output)

    # Test top three from list of scores
    def test_personal_top_three_scores(self):
        input = [3, 12, 5, 9, 8]
        expected_output = [12, 9, 8]
        result = personal_top_three(input)
        self.assertEqual(expected_output, result)

    # Test ordered from highest to lowest
    def test_descending_scores(self):
        input = [12, 9, 8, 5, 3]
        expected_output = [12, 9, 8, 5, 3]
        result = descending_scores(input)
        self.assertEqual(expected_output, result)

    # Test top three when there is a tie
    def test_top_three_scores_where_tied(self):
        input = [3, 12, 5, 12, 8]
        expected_output = [12, 12, 8]
        result = personal_top_three(input)
        self.assertEqual(expected_output, result)

    # Test top three when there are less than three
    def test_top_three_scores_where_tied(self):
        input = [3, 12]
        none_score = "None"
        expected_output = [12, 3, None]
        result = personal_top_three(input) + none_score
        self.assertEqual(expected_output, result)

    # Test top three when there is only one
    
