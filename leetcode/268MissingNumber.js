function missingNumber(nums) {
    // const numSet = new Set(nums);

    // for (let i = 0; i <= nums.length; i++) {
    //     if (!numSet.has(i)) {
    //         return i;
    //     }
    // }

    // return -1;

    const n = nums.length;
    let expectedSum = (n * (n + 1)) / 2;
    let actualSum = 0;

    for (let i = 0; i < n; i++) {
        actualSum += nums[i];
    }

    return expectedSum - actualSum;
};