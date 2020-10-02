"""
Given a list of integers and a target value, return the indices of the two numbers in the list that add up to a specific target.

*Note: You can assume that each input has exactly one solution, and the same element cannot be used more than once.*

Example:

Given nums = [3, 8, 12, 17], target = 15,

Because nums[0] + nums[2] = 3 + 12 = 15,
return [0, 2].
"""

#UPER - Understand, Plan, Execute, Reflect and Revise.

# U - What's our input? : nums (list of integers) , target (int)
    # return the indices
    #nums can be arbitrary length.
    # Edge cases: - what is no combo of numbers sum up to the target? -- we're told we can assume each input has exactly one solution.
# P - can't sort the list, because we lose the indices. 

def two_sum(nums, target):
    # how do we return the index and not the value?
    # iterate over nums list using range so that we have access to the indices.
    for index1 in range(len(nums)):
        #check if the current number + any of the rest of the numbers == target
        # use another loop to go over the rest of the numbers:
        for index2 in range(index1, len(nums)):
            #sum them up and compare against the target
            sum = nums[index1] + nums[index2]
            # if they're equal:
            if sum == target:
                #grab their indices and return them as a list [num1, num2]
                return [index1, index2]

result = two_sum([3, 8, 12, 17], 15)
print(result)
# def two_sum(nums, target):
#     # Your code here
#     return_array = [numb[0]]
#     for i in range (len(nums) -1)
#     if sum(nums[0] + nums[i]) == target:
#         return_array.append(num[i])
#     print(nums[i])
#         return return_array
#     print(two_sum([3, 8, 12, 17], 15))

# def equalto (listnum, total):
# for i in range(len(listnum)):
#     for numbers in listnum:
#         if listnum[i] + numbers == 
# 