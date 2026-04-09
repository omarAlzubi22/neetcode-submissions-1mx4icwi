class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        productArray = []
        zeroCount = 0
        total = 1
   
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
            else:
                total = total * nums[i]

        if zeroCount >= 2:
            productArray = [0] * len(nums)
            return productArray

        for i in range(len(nums)):
            if zeroCount > 0 and nums[i] == 0:
                productArray.append(total)
            elif zeroCount > 0 and nums[i] != 0:
                productArray.append(0)
            else:
                product = total // nums[i]
                productArray.append(product)
        
        return productArray
        
        


        