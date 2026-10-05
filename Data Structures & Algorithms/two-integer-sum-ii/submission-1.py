class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l + 1, r + 1]
            elif (target - sum) > 0:
                # target - sum = positive
                # we need a higher number so move l ptr to the right
                l += 1
            else:
                # the calc is negative, so now we need to increment right
                r -= 1