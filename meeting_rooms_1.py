"""
Meeting Rooms (Easy)

LeetCode - Premium Problem
NeetCode

Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.
"""

#Definition of Interval:
# Object (not a List [] or Tuple())
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        # Sort "intervals" object based on start times.
        # Return value will be i => start value = intervals[i]
        intervals.sort(key=lambda i: i.start)

        for index in range(1 , len(intervals)):
            index1 = intervals[index - 1]
            index2 = intervals[index]

            if index1.end > index2.start:
                return False
        return True