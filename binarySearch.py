# Problem
# We're given a stack of cards with integers.
# The cards are arranged in decreasing order.
# The cards are upside down so we don't know which is which.

# Requirement
# We're asked to find a given integer within the cards.
# We want to turn over as few cards as possible.

# Initial approach
# Using a sorted array, one can drastically reduce the search time by bifurcating the array.
# Step 1)
# Find the midpoint
# Step 2)
# Check the midpoint value to see if it's larger or smaller than our target number.
# Depending on larger/smaller, we'll bifurcate the array again in one direction or the other.
# Step 3)
# if mid = target, return index, else repeat steps 1 & 2, until answer is found.

# E.g.
# Let's say we're looking for the number 8, given the array below.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# mid = low + (high-low)/2
# low = 0
# high = 10
# Binary search iterations
# 1) mid = 0 + 10/2 = 5
# 2) since 5 < 8, low = 5

# 1) mid 5 + 5/2 = 7
# 2) since 5 < 8, low = 7

# 1) mid = 7 + 3/2 = 8
# 2) Found target! woo

# Given sorted array
nums = [0, 1, 3, 4, 7, 10, 11, 13, 15, 16, 17, 18,
        20, 21, 22, 23, 24, 27, 29, 31, 37, 40, 41]
low = 0
high = len(nums) - 1
target = 31
iteration = 1
while (low <= high):
    M = (low + high)/2
    if (nums[M] < target):
        low = M + 1
    elif (nums[M] > target):
        high = M - 1
    else:
        print("Found target " + str(target) + " at index " +
              str(M) + " in " + str(iteration) + " iterations.")
        break
    iteration += 1
