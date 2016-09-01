import time


# Solution 1 - Intermediate Array
def intermediate_array(n, k):
    arr = list(range(n))
    if k>n:
        k = k%n
    result = []
    for i in range(k):
        result.append(arr[n-k+i])
    for j in range(n-k):
        result.append(arr[j])
    return result


# Solution 2 - Bubble Rotate
def bubble_rotate(n, k):
    arr = list(range(n))
    for i in range(k):
        for j in range(n-1):
            temp = arr[n-1-j]
            arr[n-1-j] = arr[n-2-j]
            arr[n-2-j] = temp
    return arr


# Solution 3 - Reversal
def reverse(arr, left, right):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
    return arr


def rotate(n, k):
    if k > n:
        k = k%n
    a = n - k
    arr = list(range(n))
    arr = reverse(arr,0,a-1)
    arr = reverse(arr,a,n-1)
    arr = reverse(arr,0,n-1)
    return arr


if __name__ == "__main__":
    N,K = 10, 5

    # Solution 1:
    t1 = time.time()
    ia = intermediate_array(N,K)
    t2 = time.time()
    print("intermediate_array: %s in %2.5f s" % (ia,t2-t1))

    # Solution 2:
    t1 = time.time()
    ia = bubble_rotate(N,K)
    t2 = time.time()
    print("bubble_rotate: %s in %2.5f s" % (ia,t2-t1))

    # Solution 2:
    t1 = time.time()
    ia = rotate(N,K)
    t2 = time.time()
    print("rotate: %s in %2.5f s" % (ia,t2-t1))
