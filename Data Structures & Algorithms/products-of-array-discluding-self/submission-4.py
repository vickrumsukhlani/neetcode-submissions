class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        prefix_product = 1
        suffix_product = 1
        prefix = []
        suffix = []
        solution = []
        for num in nums:
            prefix.append(prefix_product)
            prefix_product *= num
        
        for i in range(len(nums) - 1, -1, -1):
            suffix.append(suffix_product)
            suffix_product *= nums[i]

        suffix.reverse()

        for i in range(len(nums)):
            solution.append(prefix[i] * suffix[i])

        return solution





    # product = 1
    # zero_count = 0
    # zero_index = 0

    # for index, value in enumerate(nums):
    #     if value == 0:
    #         zero_count += 1
    #         zero_index = index
    #     else: 
    #         product *= value


    # if zero_count >= 2:
    #     return [0] * len(nums)

    # if zero_count == 1:
    #     solution = [0] * len(nums)
    #     solution[zero_index] =  product
    #     return solution

    # solution = []

    # for value in nums:
    #         solution.append(product // value)

    # return solution