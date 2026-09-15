class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Base problem you coudl compute 
        product = 1
        zero_count = 0
        solution = []
        for index, value in enumerate(nums):
            if value == 0:
                zero_count += 1
            else: 
                product *= value


        if zero_count >= 2:
            solution = [0] * len(nums)
            return solution


        for i in range(len(nums)):
            if nums[i] == 0:
                solution = [0] * len(nums)
                solution[i] = product
                return solution
            else:
                solution.append(product // nums[i])

        return solution