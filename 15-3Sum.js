/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    nums.sort((a, b) => (a-b));
    res = [];

    for (let i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) {
            continue;
        }

        const target = nums[i];

        l = i + 1;
        r = nums.length - 1;

        while (l < r) {
            sum = nums[l] + nums[r] + target;
            if (sum === 0) {
                res.push([target, nums[l], nums[r]]);
                l++;
                r--;
                
                while(l < r && nums[l] === nums[l-1]) l++;
                while(l < r && nums[r] === nums[r+1]) r--;
            }
            else if (sum < 0){
                l++;
            }
            else {
                r--;
            }
        }
    }
    return res
};