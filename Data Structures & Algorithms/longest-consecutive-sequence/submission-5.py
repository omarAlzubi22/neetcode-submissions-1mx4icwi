class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        curLongest = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in nums:
                curIndex = nums[i]
                curSequence = 1
                if curSequence > curLongest:
                        curLongest = curSequence
                while curIndex + 1 in nums:
                    curSequence += 1
                    if curSequence > curLongest:
                        curLongest = curSequence
                    curIndex += 1
        return curLongest
                            

        

        