class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        len_coins = len(coins)
        table = [[0 for y in range(amount+1)]for x in range(len_coins+1)]
        
        
        maxint = sys.maxsize
        for j in range(1, amount+1):
            table[0][j] = maxint
                
        for i in range(1, len_coins+1):
            for j in range(1, amount+1):
                if coins[i-1] > j:
                    table[i][j] = table[i-1][j]
                else:
                    table[i][j] = min(table[i-1][j] , 1+ table[i][j-coins[i-1]])
                    
        if table[len_coins][amount] != sys.maxsize:
            return table[len_coins][amount]
        else:
            return -1
                
                
        