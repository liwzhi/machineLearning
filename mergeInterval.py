# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 22:49:01 2015

@author: weizhi
"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals)==0:
            return 
        result = []
        pre = intervals.pop()
        while(intervals):
            curr = intervals.pop()
            if curr.start-pre.end<0:
                pre.start = min(pre.start,curr.start)
                pre.end = min(pre.end,curr.end)
                intervals.append(pre)
            result.append(pre)
            pre = curr
        return result.append(pre)