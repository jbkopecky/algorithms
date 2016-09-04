import urllib2
import heapq

ALPH = 'abcdefghijklmnopqrstuvwxyz'
DICT_URL = 'https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co&pathrev=61569'


def get_words(length):
    data = urllib2.urlopen(DICT_URL)
    words = [w.strip().lower() for w in data if len(w.strip()) == length]
    return words


def word_ladder(start_word, end_word, word_set):
    queue = [(1, start_word)]
    word_set.add(end_word)

    while len(queue) > 0:
        numstep, word = queue.pop(0)

        if word == end_word:
            return numstep

        arr = list(word)

        for i in range(len(arr)):
            for c in ALPH:
                if arr[i] == c:
                    continue
                temp = arr[i]
                arr[i] = c
                new_word = ''.join(arr)
                arr[i] = temp
                if new_word in word_set:
                    word_set.remove(new_word)
                    queue.append((numstep + 1, new_word))
    return 0


if __name__ == "__main__":
    from_word = 'hit'
    to_word = 'cog'
    
    short_set = set(["hot","dot","dog","lot","log"]) 
    print(word_ladder(from_word, to_word, short_set))
    
    words_set = set(get_words(len(from_word)))
    print(word_ladder(from_word, to_word, words_set))
