class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_list = sorted(set(nums))

        if len(sorted_list) == 0:
            return 0

        current_seq = 1
        longest_seq = 1

        for x in range(len(sorted_list) - 1):
            if (sorted_list[x] + 1) == sorted_list[x + 1]:
                current_seq += 1
            else:
                current_seq = 1

            longest_seq = max(current_seq, longest_seq)
        
        return longest_seq