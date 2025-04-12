"""
Meeting Rooms II
Medium Difficulty
NeetCode

Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.
"""

"""
Definition of Interval:
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals) -> int:
        start_array = sorted([i.start for i in intervals])
        end_array = sorted([i.end for i in intervals])

        result = 0
        count = 0
        s = 0
        e = 0

        while s < len(intervals):
            if start_array[s] < end_array[e]:
                s += 1
                count += 1
            else:
                # If start and end times are matching, then handle end-time first (move end-time to next element in end_array), start-time second.
                e += 1
                count -= 1
            result = max(result, count)

        return result