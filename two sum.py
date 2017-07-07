class Solution(object):
	def twosum(self, nums, target):
		if len(nums)<0:
			return False
		for i in range(len(nums)):
			for j in range(len(nums)):
				if nums[i]+nums[j] == target:
					return [i,j]
					