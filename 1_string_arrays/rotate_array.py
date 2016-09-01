from utils import timeit


# Solution 1 - Intermediate Array
@timeit
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
    N = 10
    K = 4
    ia = intermediate_array(N,K)
    print(ia)




