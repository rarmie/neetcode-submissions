class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max_area = 0

        # for l in range(len(heights)):
        #     for r in range(len(heights)):
        #         if l == r:
        #             continue

        #         height = min(heights[l], heights[r])
        #         width = abs(l - r)

        #         current_area = height * width

        #         if current_area > max_area:
        #             max_area = current_area
                
        # return max_area


        max_area = 0 
        first_bar = 0
        second_bar = len(heights) - 1

        while first_bar != second_bar:
            height = min(heights[first_bar], heights[second_bar])
            width = abs(first_bar - second_bar)

            current_area = height * width

            if current_area > max_area:
                max_area = current_area

            if heights[first_bar] >= heights[second_bar]:
                second_bar -= 1
            else:
                first_bar += 1

        return max_area


            
            


            
            

