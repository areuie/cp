/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    freq = {};
    for (let i = 0; i < nums.length; i++) {
        if (freq[target-nums[i]] !== undefined) {
            return [i, freq[target-nums[i]]];
        }
        freq[nums[i]] = i;
    }
};