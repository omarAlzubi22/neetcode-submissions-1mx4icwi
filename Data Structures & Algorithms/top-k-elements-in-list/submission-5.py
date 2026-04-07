class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        HashMap = {}
        listK = []

        for i in range(len(nums)):
            if nums[i] in HashMap:
                HashMap[nums[i]] += 1
            else:
                HashMap[nums[i]] = 1

        buckets = [[] for i in range(len(nums) + 1)]
        for num, count in HashMap.items():
            buckets[count].append(num)

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                listK.append(num)
                if len(listK) == k:
                    return listK


                    