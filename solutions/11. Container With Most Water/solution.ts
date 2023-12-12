function maxArea(height: number[]): number {
  let largestArea = 0;
  let i = 0;
  let j = height.length - 1;
  while (i < j) {
    largestArea = Math.max(largestArea, (j - i) * Math.min(height[i], height[j]));
    if (height[i] <= height[j]) {
      i++;
    } else {
      j--;
    }
  }
  return largestArea;
};
