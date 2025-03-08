class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minimum = maximum = prices[0]
        profit = 0
        for i in prices:
            if i > minimum:
                maximum = i
                profit += maximum - minimum
                minimum = maximum = i
            if i < minimum:
                minimum = i
                maximum = i
        return profit

prices = [7,1,5,3,6,4]
a = Solution().maxProfit(prices=prices)
print(a)
