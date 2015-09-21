# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 23:25:26 2015

@author: weizhi
"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        if 9*k<n:
            return result
        self.helper(n,result,0,[],n,k)
        return result
    def helper(self,n,result,start,stk,target,k):
       # if 9*k<n:
        #    return 
        if target<0:
            return 
        if target==0 and k ==0:
            result.append(stk[:])
        for item in range(start,9):
            self.helper(n,result,item+1,stk+[item+1],target-item-1,k-1)
Obj = Solution()
result = Obj.combinationSum3(2,9)
print result