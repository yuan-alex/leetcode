class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(0, len(image)):
            image[row].reverse()
            for i in range(0, len(image[row])):
                if image[row][i] == 1:
                    image[row][i] = 0
                else:
                    image[row][i] = 1
        return image