'''
Created on Dec 22, 2018

@author: omid
'''

import unittest


def merge_ranges(meeting_times):
    # This sorts the touple based on the first element
    if len(meeting_times) < 2:
        return meeting_times
    meeting_time_sorted = sorted(meeting_times)
    merged_meeting_time = []
    merged_meeting_time.append(meeting_time_sorted[0])
    
    for meeting_time in range(1, len(meeting_time_sorted)):
        start_time, end_time = meeting_time_sorted[meeting_time]
        last_start_merged, last_end_merged = merged_meeting_time[-1]
        # See the and is important! Otherwise you can not detect 
        # the case the last one contains the next one!
        # Actually this is an edge case for the first meeting ends after the
        # second meeting
        # Either of the following works fine! Just make sure you check somehow for 
        # the end time as well!
        #if (last_end_merged >= start_time) and (last_end_merged < end_time):
        #   merged_meeting_time[-1] = (last_start_merged, end_time)
        if (last_end_merged >= start_time):
            merged_meeting_time[-1] = (last_start_merged, max(last_end_merged, end_time))
        elif last_end_merged < start_time:
            merged_meeting_time.append((start_time, end_time))
        
    return merged_meeting_time
    
    
            
            
        


















# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
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

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
