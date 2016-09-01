import time

# Solution 1 - Intermediate Array
def intermediate_array(n, k):
    arr = range(n)
    if k>len(arr):
        k = k%len(arr)
    result = []
    for i in range(k):
        result.append(arr[n-k+i])
    for j in range(n-k):
        result.append(arr[j])
    return result

# Solution 2 - Bubble Rotate
def bubble_rotate(n, k):
    arr = range(n)
    for i in range(k):
        for j in range(n-1):
            temp = arr[n-1-j]
            arr[n-1-j] = arr[n-2-j]
            arr[n-2-j] = temp
    return arr


if __name__ == "__main__":

    N,K = 10, 12

    # Solution 1:
    t1 = time.time()
    ia = intermediate_array(N,K)
    t2 = time.time()
    print("intermediate_array: %s in %2.4f s" % (ia,t2-t1))

    # Solution 2:
    t1 = time.time()
    ia = bubble_rotate(N,K)
    t2 = time.time()
    print("intermediate_array: %s in %2.4f s" % (ia,t2-t1))
