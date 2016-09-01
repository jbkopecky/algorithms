def rotate_words(string):
    j = 0
    for i, s in enumerate(string):
        if s == ' ':
            string = reverse(string, j, i-1)
            j = i + 1

    string = reverse(string, j, len(string)-1)
    string = reverse(string, 0, len(string)-1)

    return string

def reverse(string, left, right):
    string = list(string)
    # Python strings are immutable so they do not support assignment.
    # So we cast the string into a list first, and we join the list into a str
    # at the end before returning.
    if len(string) == 0 or len(string) == 1:
        return string
    while left < right:
        temp = string[left]
        string[left] = string[right]
        string[right] = temp
        left += 1
        right -= 1
    string = "".join(string)
    return string

if __name__ == "__main__":
    string = 'the sky is blue'
    ginrts = rotate_words(string)
    print(ginrts)

