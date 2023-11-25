/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const numsSet = new Set(nums);
    const isEqual = numsSet.size === nums.length;

    return !isEqual;
};

console.log(containsDuplicate([2,14,18,22,22]))
