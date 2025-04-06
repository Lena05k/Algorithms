function containsNearbyDuplicate(nums, k) {
    let map = new Map();

    for (let i = 0; i < nums.length; i++) {
        if (map.has(nums[i])) {
            if ((i - map.get(nums[i])) <= k) {
                return true;
            }
        }
        map.set(nums[i], i);
    }
    // for (let i = 0; i < nums.length; i++) {
    //     for (let j = i + 1; j < nums.length; j++) {
    //         if (nums[i] === nums[j] && Math.abs(i - j) <= k) {
    //             return true;
    //         }
    //     }
    // }

    return false;
};