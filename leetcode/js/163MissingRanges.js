function findMissingRanges(lover, upper, nums) {
    const missingRanges = [];
    let prev = lover - 1;

    for (let i = 0; i <= nums.length; i++) {
        const curr = (i < nums.length - 1) ? nums[i] : upper + 1;
        if (prev + 1 <= curr -1 ) {
            missingRanges.push([prev + 1, curr - 1]);
        }
        prev = curr;
    }
    return missingRanges;
}