class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        sorted_dict = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
        values = list(sorted_dict.keys())

        top_k = []
        for i in range(0, k):
            top_k.append(values[i])

        return top_k