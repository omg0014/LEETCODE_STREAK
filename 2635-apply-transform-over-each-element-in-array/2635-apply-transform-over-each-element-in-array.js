/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const result = [];

    for (let i = 0; i < arr.length; i++) {
        result.push(fn(arr[i], i));  // apply fn to each element
    }

    return result;
};
