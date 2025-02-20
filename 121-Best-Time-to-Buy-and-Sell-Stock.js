/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    minPrice = Infinity;
    res = 0;
    for (const price of prices) {
        minPrice = Math.min(minPrice, price);
        res = Math.max(res, price - minPrice);
    }
    return res;
};