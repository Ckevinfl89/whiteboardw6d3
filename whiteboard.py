# Problem 3:
# 3 Sum 
# What if we now look for triplets, and not pairs, that add up to a target (in this case, our target is always 0)
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# Also, notice, we are not worried about the index of the triplet but the actual values instead.
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
# Constraints:
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

def solution(nums):
  """
  Finds all triplets in nums that add up to 0.

  Args:
    nums: An array of integers.

  Returns:
    A list of all triplets in nums that add up to 0.
  """

  triplets = []
  nums.sort()

  for i in range(len(nums) - 2):
    # Skip duplicates.
    if i > 0 and nums[i] == nums[i - 1]:
      continue

    target = -nums[i]
    j = i + 1
    k = len(nums) - 1

    while j < k:
      sum = nums[j] + nums[k]
      if sum == target:
        triplets.append([nums[i], nums[j], nums[k]])
        j += 1
        while j < k and nums[j] == nums[j - 1]:
          j += 1
      elif sum < target:
        j += 1
      else:
        k -= 1

  return triplets

def solution(nums):
    n = len(nums)
    nums.sort()
    result = []
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates
        
        left, right = i + 1, n - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1  # Skip duplicates
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1  # Skip duplicates
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result

def solution(arrNums):
    target = 0
    tempList = []
    for i in range(len(arrNums)-1):
        arrNums2 = arrNums[:]
        arrNums2.pop(i)
        for j in range(len(arrNums2)-1):
            arrNums3 = arrNums2[:]
            arrNums3.pop(j)
            for k in range(len(arrNums3)-1):
                if (arrNums[i] + arrNums2[j] + arrNums3[k]) == target:
                    tempList.append([arrNums[i], arrNums2[j], arrNums3[k]])
    
    retList = []
    for item in tempList:
        item.sort()
        if item not in retList:
            retList.append(item)
    return retList
