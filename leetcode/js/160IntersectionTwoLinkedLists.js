function getIntersectionNode(headA, headB) {
    const nodeSet = new Set();

    let current = headA;
    while (current) {
        nodeSet.add(current);
        current = current.next;
    }

    current = headB;
    while (current) {
        if (nodeSet.has(current)) {
            return current;
        }

        current = current.next;
    }

    return null;
};