/**
 * @param {number[][]} matrix
 * @return {number}
 */
var minFallingPathSum = function(matrix) {
    // dp where base case is bottom, return grid, try calling from whole top row 
    // bot, left, right
    function minFallingPath(i, j) {
        if (i < 0 || j < 0 || i >= n || j >= m) return Infinity;
        if (i == n - 1) return matrix[i][j];
        if (dp[i][j] !== Infinity) return dp[i][j];

        let bLeft = matrix[i][j] + minFallingPath(i + 1, j - 1);
        let bottom = matrix[i][j] + minFallingPath(i + 1, j);
        let bRight = matrix[i][j] + minFallingPath(i + 1, j + 1);

        dp[i][j] = Math.min(bLeft, bottom, bRight);

        return dp[i][j];
    }
    let n = matrix.length;
    let m = matrix[0].length;
    let dp = new Array(n).fill(Infinity).map(()=>new Array(m).fill(Infinity));

    let res = Infinity;
    for(let j = 0; j < m; j++) {
        res = Math.min(res, minFallingPath(0, j));
    }
    return res;
};