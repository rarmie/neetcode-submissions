class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_groups = defaultdict(int)
        most_frequent = []

        for x in nums:
            num_groups[x] += 1

        sorted_dict = sorted(num_groups.items(), key = lambda x: x[1], reverse = True)

        sorted_list = [x[0] for x in sorted_dict]

        for x in range(k):
            most_frequent.append(sorted_list[x])

        return most_frequent