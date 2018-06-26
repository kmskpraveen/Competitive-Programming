import unittest


def merge_ranges(meetings):

    # Merge meeting ranges
    meetings.sort()
    updatedList = []
    
    for i in range(len(meetings)):
        meetings[i] = list(meetings[i])

    updatedList.append(meetings[0])

    for current in meetings[1:]:
        if current[0]<=updatedList[len(updatedList)-1][1]:
            updatedList[len(updatedList)-1][1] = max(current[1],updatedList[len(updatedList)-1][1])
        else:
            updatedList.append(current)

    for i in range(len(updatedList)):
        updatedList[i] = tuple(updatedList[i])
        
    return updatedList


















# Tests

class Test(unittest.TestCase):

    # def test_meetings_overlap(self):
    #     actual = merge_ranges([(1, 3), (2, 4)])
    #     expected = [(1, 4)]
    #     self.assertEqual(actual, expected)

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 5), (2, 3)])
        expected = [(1, 5)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
