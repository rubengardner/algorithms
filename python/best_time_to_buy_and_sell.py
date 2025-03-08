class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minimum = maximum = prices[0]
        profit = 0
        for i in prices:
            if i >= maximum:
                maximum = i
                if profit < maximum - minimum:
                    profit = maximum - minimum
            if i < minimum:
                minimum = i
                maximum = i
        return profit


prices = [3,2,6,5,0,3]
a = Solution().maxProfit(prices=prices)
print(a)



