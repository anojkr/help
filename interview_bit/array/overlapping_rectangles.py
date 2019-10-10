Given eight integers A, B, C, D, E, F, G and H which represent two rectangles in a 2D plane.

For the first rectangle it’s bottom left corner is (A, B) and top right corner is (C, D) and
for the second rectangle it’s bottom left corner is (E, F) and top right corner is (G, H).

class Solution:
    
    def solve(self, A, B, C, D, E, F, G, H):
            start_x = max(A, E)
            end_x = min(C, G)
            a = 1
            width = end_x - start_x
            if width <= 0:
                a = 0
                
            start_y = max(B, F)
            end_y = min(D, H)
            
            height = end_y - start_y
            if height <=0:
                a = 0
                
            area = width*height
            return a
            