class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_list = sorted(set(nums))

        if nums == []:
            return 0
        longest_seq = 1
        current_seq = 1

        for i in range(len(sorted_list) - 1):
            if sorted_list[i + 1] == sorted_list[i] + 1:
                current_seq += 1
            else:
                if current_seq > longest_seq:
                    longest_seq = current_seq

                current_seq = 1
        
        if current_seq > longest_seq:
            longest_seq = current_seq

        return longest_seq