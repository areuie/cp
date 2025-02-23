/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    // flip across diagonal
    // flip across vertical
    let n = matrix.length;
    let m = matrix[0].length;

    for(let i = 0; i < n; i++) {
        for(let j = i; j < m; j++) {
            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
        }
    }

    for(let i = 0; i < n; i++) {
        for(let j = 0; j < Math.ceil(m / 2); j++) {
            [matrix[i][j], matrix[i][m-j-1]] = [matrix[i][m-j-1], matrix[i][j]];
        }
    }
};