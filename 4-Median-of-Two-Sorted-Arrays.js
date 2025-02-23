var findMedianSortedArrays = function(A, B) {
    let M = A.length + B.length;
    let n1 = A.length;
    let n2 = B.length;

    let pA = 0;
    let pB = 0;

    let prev = 0;
    let curr = 0;

    function findMin() {
        if(pA < n1 && pB < n2) {
            if(A[pA] <= B[pB]) return A[pA++];
            else return B[pB++];
        }
        return (pA < n1) ? A[pA++] : B[pB++];
    }

    for(let i = 0; i <= Math.floor(M / 2); i++) {
        prev = curr;
        curr = findMin();
    }

    if (M % 2 == 1) return curr;
    return (prev + curr) / 2;
};
