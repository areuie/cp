/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    let n = grid.length;
    let m = grid[0].length;
    
    let prev = new Array(m).fill(-1);

    for(let i = 0; i < n; i++) {
        let curr = new Array(m).fill(-1);
        for(let j = 0;j < m; j++) {
            if (i === 0 && j === 0) {
                curr[j] = grid[i][j];
            } else {
                let left = Infinity;
                let up = Infinity;

                if (j > 0) left = grid[i][j] + curr[j-1];
                if (i > 0) up = grid[i][j] + prev[j];

                curr[j] = Math.min(left, up);
            }
        }
        prev = curr;
    }
    return prev[m-1];
};