class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        flbed = [0] + flowerbed + [0]

        result = 0

        for i in range(1, len(flbed)-1):
            if flbed[i-1] == 0 and flbed[i+1] == 0 and flbed[i] == 0:
                flbed[i] = 1
                result += 1
        
        return result >= n
