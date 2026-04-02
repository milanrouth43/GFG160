def kthSmallest(a, b, k):
    n = len(a)
    m = len(b)
    lo = 0
    hi = n
    idx = 0

    while lo <= hi:
        mid1 = (lo + hi) // 2
        mid2 = k - mid1
        if mid2 > m:
            lo = mid1 + 1
            continue
        l1 = a[mid1 - 1] if mid1 > 0 else float('-inf')
        r1 = a[mid1] if mid1 < n else float('inf')
        l2 = b[mid2 - 1] if mid2 > 0 else float('-inf')
        r2 = b[mid2] if mid2 < m else float('inf')
        if l1 <= r2 and l2 <= r1:
            idx = mid1
            break
        if l1 > r2:
            hi = mid1 - 1 
        else:
            lo = mid1 + 1
            
    return idx

def mergeArrays(a, b):
    n = len(a)
    m = len(b)
    idx = kthSmallest(a, b, n)
    for i in range(idx, n):
        a[i], b[i - idx] = b[i - idx], a[i]
    a.sort()
    b.sort()

if __name__ == "__main__":
    a = [1, 5, 9, 10, 15, 20]
    b = [2, 3, 8, 13]
    mergeArrays(a, b)

    for ele in a:
        print(ele, end=" ")
    print()
    for ele in b:
        print(ele, end=" ")
