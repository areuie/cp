/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    function minSum(i, j) {
        if (i === 0 && j === 0) {
            return grid[i][j];
        }

        if (dp[i][j] !== -1) {
            return dp[i][j];
        }
        
        let left = Infinity;
        let up = Infinity;

        if (j > 0) left = grid[i][j] + minSum(i,j-1);
        if (i > 0) up = grid[i][j] + minSum(i-1,j);

        dp[i][j] = Math.min(left, up);
        return dp[i][j];
    }

    let n = grid.length;
    let m = grid[0].length;
    
    let dp = new Array(n).fill(-1).map(() => {
       return new Array(m).fill(-1)
    });

    return minSum(n-1, m-1);
};