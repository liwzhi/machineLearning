# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 21:29:54 2015

@author: weizhi
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        marked = [[False for i in range(col)] for j in range(row)] # create mark
        count =0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1' and not marked[i][j]:
                    self.DFS(grid,marked,row,col,i,j)
                    count+=1
        return count
            
    
    def DFS(self,grid,marked,row,col,x,y):
        if grid[x][y] == '0' or marked[x][y]:
            return 
        marked[x][y] =True
        if x!=0:
            self.DFS(grid,marked,row,col,x-1,y)
        if x!=row-1:
            self.DFS(grid,marked,row,col,x+1,y)
        if y!=0:
            self.DFS(grid,marked,row,col,x,y-1)
        if y!=col-1:
            self.DFS(grid,marked,row,col,x,y+1)
        
        