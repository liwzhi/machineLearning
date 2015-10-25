# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 15:46:22 2015

@author: weizhi
"""
#Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#    For example, given array S = {-1 2 1 -4}, and target = 1.
#
#    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution1(object):
    minValue = float('inf')
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = sum(nums[:3])
        for low in range(len(nums)):
            mid = low+1
            high = len(nums)-1
            while mid<high:
                sumValue = nums[low]+nums[mid]+nums[high]
                if abs(sumValue-target)<abs(res-target):
                    res = sumValue
                if sumValue>target:
                    high-=1
                elif sumValue<target:
                    mid+=1
                else:
                    return res
        return res

                





class Solution(object):
    minValue = 2**31
    result = float('inf')
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)<3:
            return 
        return self.helper(sorted(nums),target,[],0)
    
    def helper(self,nums,target,stk,start):
     #   print stk
        if len(stk)==3:
            absValue = abs(target-sum(stk))
            if absValue<self.minValue:
                self.minValue = absValue
                self.result = stk
                return self.result
        for i in range(start,len(nums)):
            if len(stk)<=3:
                stk = stk + [nums[i]]
                self.helper(nums,target,stk,i+1)
                stk.pop()
        return self.result
                
a = [-43,57,-71,47,3,30,-85,6,60,-59,0,-46,-40,-73,53,68,-82,-54,88,73,20,-89,-22,39,55,-26,95,-87,-57,-86,28,-37,43,-27,-24,-88,-35,82,-3,39,-85,-46,37,45,-24,35,-49,-27,-96,89,87,-62,85,-44,64,78,14,59,-55,-10,0,98,50,-75,11,97,-72,85,-68,-76,44,-12,76,76,8,-75,-64,-57,29,-24,27,-3,-45,-87,48,10,-13,17,94,-85,11,-42,-98,89,97,-66,66,88,-89,90,-68,-62,-21,2,37,-15,-13,-24,-23,3,-58,-9,-71,0,37,-28,22,52,-34,24,-8,-20,29,-98,55,4,36,-3,-9,98,-26,17,82,23,56,54,53,51,-50,0,-15,-50,84,-90,90,72,-46,-96,-56,-76,-32,-8,-69,-32,-41,-56,69,-40,-25,-44,49,-62,36,-55,41,36,-60,90,37,13,87,66,-40,40,-35,-11,31,-45,-62,92,96,8,-4,-50,87,-17,-64,95,-89,68,-51,-40,-85,15,50,-15,0,-67,-55,45,11,-80,-45,-10,-8,90,-23,-41,80,19,29,7]
               
obj = Solution()
print obj.threeSumClosest(a,255)