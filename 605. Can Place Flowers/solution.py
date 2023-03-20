class Solution:
  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    if n == 0:
      return True
    if len(flowerbed) == 1:
      return n - flowerbed[0] > 0
    for i in range(len(flowerbed)):
      if flowerbed[i] == 1:
        continue
      if i == 0 and flowerbed[i + 1] == 0:
        flowerbed[i] = 1
        n -= 1
      elif i == len(flowerbed) - 1 and flowerbed[i - 1] == 0:
        flowerbed[i] = 1
        n -= 1
      elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
        flowerbed[i] = 1
        n -= 1
      if n == 0:
        return True
    return False
