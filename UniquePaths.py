class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 for i in range(n+1)] for j in range(m+1)]
        
        for i in range(2,m+1):
            for j in range(2,n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]