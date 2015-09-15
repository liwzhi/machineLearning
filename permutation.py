# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 09:50:25 2015

@author: weizhi
"""

class Solution(object):
    def permute(self,num):
        result = []
        used = [False]*len(num)
        self.helper(result,used,[],num)
    def helper(self,result,used,curr,num):
        if len(curr) == len(num):
            result.append(curr + [])
            return
        for i in range(len(num)):
            if not used[i]:
                used[i]= True
                curr.append(num[i])
                self.helper(result,used,curr,num)
                curr.pop()
                used[i] = False
# features
# map reduce
# explore the data sets, new clients, unique, deal scale the machine learing 
# engineer
            
    