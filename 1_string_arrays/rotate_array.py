import time

# Solution 1 - Intermediate Array
def intermediate_array(n, k):
    array = range(n)
    if k>len(array):
        k = k%len(array)
    result = []
    for i in range(k):
        result.append(array[len(array)-k+i])
    for j in range(len(array)-k):
        result.append(array[j])
    return result

if __name__ == "__main__":
    t1 = time.time()
    ia = intermediate_array(10,4)
    t2 = time.time()
    print("intermediate_array: %s in %2.4f s" % (ia,t2-t1))

