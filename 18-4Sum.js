/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {

    nums.sort((a,b) => (a-b));
    return kSum(nums, 4, target, 0);

    function kSum(nums, k, target, start) {

        if (k === 2) return twoSum(nums, target, start);        

        let n = nums.length;
        let res = []; 

        for(let i = start;i < n; i++) {
            if (i > start && nums[i-1] === nums[i]) continue;
            let subResults = kSum(nums, k-1, target-nums[i], i + 1);
            for(let arr of subResults){
                res.push([nums[i], ...arr]);
            }
        }
        return res;
    }

    function twoSum(nums, target, start) {
        let n = nums.length;

        let l = start;
        let r = n - 1;

        let res = [];

        while(l < r) {
            if(nums[l] + nums[r] === target) {
                res.push([nums[l], nums[r]]);
                l++;
                r--;

                while (l < r && nums[l - 1] === nums[l]) l++;
                while (l < r && nums[r+1] === nums[r]) r--;
            } else if (nums[l] + nums[r] < target) l++;
            else r--;
        }
        return res;
    }
};