"""Given an integer n, return a string array answer (1-indexed) where:
    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.
Example 1:
Input: n = 3
Output: ["1","2","Fizz"]
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """Soltion 1"""
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]

        """Solution 2"""
        # num = []
        # for i in range(1,n+1):
        #     if i % 3 == 0 and i % 5 == 0:
        #         num.append("FizzBuzz")
        #     elif i % 3 == 0:
        #         num.append("Fizz")
        #     elif i % 5 == 0:
        #         num.append("Buzz")
        #     else:
        #         num.append(str(i))
        # return num