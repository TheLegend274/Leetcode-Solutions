def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1
        maxP = 0
        while(r < len(prices)):
            #is it profitable?
            if(prices[r] > prices [l]):
                profit = prices[r] - prices[l]
                maxP = max(maxP,profit)
            else:
                l = r
            r+=1
        return maxP
