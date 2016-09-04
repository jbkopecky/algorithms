def rotate_words(str):
    words = str.split(' ')
    return ' '.join(reversed(words))

if __name__ == "__main__":
    string = 'the sky is blue'
    ginrts = rotate_words(string)
    print(ginrts)
