#include <stdio.h>
/**
Given an array of integers, return indices of the two numbers such that they add
up to a specific target.
You may assume that each input would have exactly one solution, and you may not
use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

 */

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void printArray(int *arr, int xsize);

int *twoSum(int *nums, int numsSize, int target) {
  static int res[2] = {0};
  for (int i = 0; i < numsSize; ++i)
    for (int j = i + 1; j < numsSize; ++j)
      if (nums[i] + nums[j] == target) {
        res[0] = i;
        res[1] = j;
      }
  return res;
}

void main() {
  int nums[4] = {2, 7, 11, 15};
  int target = 9;
  int *res = twoSum(nums, 4, target);
  printArray(res, 2);
}

void printArray(int *arr, int arrsize) {
  for (int i = 0; i < arrsize; i++)
    printf("%d ", arr[i]);
  puts("\n");
}
