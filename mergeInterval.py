# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 22:49:01 2015

@author: weizhi
"""
[[1,4],[0,2],[3,5]]
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
        pre = intervals.pop(0)
        while(len(intervals)>1):
            curr = intervals.pop()
            if curr.start-pre.end<0 and curr!=pre:
                curr.start = min(pre.start,curr.start)
                print pre.start
                curr.end = max(pre.end,curr.end)
                intervals.append(curr)  #[1,4]
                print [curr.start,curr.end]
            result.append([curr.start,curr.end])
            pre = curr #[1,4]
        return result
a = Interval(1,4)
print a.end
b = Interval(0,2)  # 0,4
c = Interval(3,5)  #0 5
data = [a,b,c]
Obj = Solution()
print Obj.merge([a,b,c])