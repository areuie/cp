/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    function steps(n) {
        if(n < 0) return 0;
        if(n === 0) return 1;
        
        if (dp[n] !== -1) return dp[n];

        let oneStep = steps(n-1);
        let twoSteps = steps(n-2);

        dp[n] = oneStep + twoSteps;
        return oneStep + twoSteps;
    }
    let dp = new Array(n+1).fill(-1);
    return steps(n);
};