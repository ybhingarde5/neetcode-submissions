class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums)+1)]

        for num, freq in count.items():
            bucket[freq].append(num)
        
        result = []
        for i in range(len(bucket) -1, 0, -1):
            if bucket[i]:
                for num in bucket[i]:
                    result.append(num)
                    if len(result) == k:
                        return result




        # hashmap = {}
        # for num in nums:
        #     if num in hashmap:
        #         hashmap[num] += 1
        #     else:
        #         hashmap[num] = 1
        
        # result = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)

        # return [value for value, freq in result[:k]]


        