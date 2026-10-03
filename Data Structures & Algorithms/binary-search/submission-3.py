class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # logn time => binary search, cut problem in half each time.

        l,r = 0, len(nums)

        while l < r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        

        return -1
