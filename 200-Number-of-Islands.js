/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    function dfs(i, j) {
        if(i < 0 || j < 0 || i >= n || j >= m || grid[i][j] === \0\) return;

        grid[i][j] = \0\;
        
        dfs(i,j-1);
        dfs(i,j+1);
        dfs(i-1,j);
        dfs(i+1,j);
    }

    let islands = 0;
    let n = grid.length;
    let m = grid[0].length;

    for(let i = 0; i < n; i++) {
        for(let j =0; j < m; j++) {
            if(grid[i][j] === \1\) {
                dfs(i, j);
                islands++;
            }
        }
    }
    return islands;
};