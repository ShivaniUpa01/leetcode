"""121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""
# Solution 1 : Kadane's Algorithm
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        curr = 0
        max_num = 0
        i = 0
        while i < len(prices):
            curr = prices[i] - prices[start]
            i += 1
            if max_num < curr:
                max_num = curr
            if curr < 0 :
                curr = 0
                start += 1
                i = start + 1
        return max_num

    #Solution 2
    class Solution:
        def maxProfit(self, prices: List[int]) -> int:
            i = 0
            j = 1
            diff = 0
            result = 0
            while j < len(prices):
                if prices[i] < prices[j]:
                    diff = prices[j] - prices[i]
                    if result < diff:
                        result = diff
                else:
                    i = j
                j += 1
            return result

        # Solution 3
        class Solution:
            def maxProfit(self, prices: List[int]) -> int:
                i = 0
                j = 1
                n = 0
                maximum = float(-inf)

                while j != len(prices):
                    if prices[i] > prices[j]:
                        i = j
                        j += 1
                    else:
                        if maximum < abs(prices[i] - prices[j]):
                            maximum = abs(prices[i] - prices[j])
                        j += 1
                if maximum == float(-inf):
                    return 0
                else:
                    return maximum
