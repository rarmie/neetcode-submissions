class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_list = sorted(set(nums))


        if not sorted_list:
            return 0

        longest_seq = 1
        current_seq = 1

        for n in range(len(sorted_list) - 1):
            if sorted_list[n + 1] == sorted_list[n] + 1:
                current_seq += 1

            else:
                if current_seq > longest_seq:
                    longest_seq = current_seq

                current_seq = 1
        
        if current_seq > longest_seq:
                    longest_seq = current_seq

        return longest_seq