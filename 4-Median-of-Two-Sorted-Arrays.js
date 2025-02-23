var findMedianSortedArrays = function (A, B) {
    let n1 = A.length;
    let n2 = B.length;

    if (n1 > n2) {
        return findMedianSortedArrays(B, A);
    }
    
    let m = n1 + n2;

    let low = 0;
    let high = n1;

    let leftPartition = Math.floor((m + 1) / 2 );

    while (low <= high) {
        let m1 = Math.floor((low + high) / 2);
        let m2 = leftPartition - m1;

        let l1 = Number.MIN_SAFE_INTEGER, l2 = Number.MIN_SAFE_INTEGER;
        let r1 = Number.MAX_SAFE_INTEGER, r2 = Number.MAX_SAFE_INTEGER;

        if (m1 - 1 >= 0) l1 = A[m1 - 1];
        if (m2 - 1 >= 0) l2 = B[m2 - 1];
        if (m1 < n1) r1 = A[m1];
        if (m2 < n2) r2 = B[m2];

        if (l1 <= r2 && l2 <= r1) {
            if (m % 2 == 1) return Math.max(l1, l2);
            return ((Math.max(l1,l2) + Math.min(r1, r2)) / 2);
        } else if(l1 > r2) {
            high = m1 - 1;
        } else {
            low = m1 + 1;
        }
    }

    return 0;
};