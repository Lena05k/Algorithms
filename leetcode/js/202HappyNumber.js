function isHappy(n) {
    const numSet = new Set();

    while (n !== 1) {
        let current = n;
        let sum = 0;

        while (current > 0) {
            let digit = current % 10;
            sum += digit**2;
            current = Math.floor(current / 10);
        }

        if (numSet.has(sum)) {
            return false;
        }

        numSet.add(sum);
        n = sum;
    }

    return true;
};