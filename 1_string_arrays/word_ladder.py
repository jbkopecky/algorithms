import urllib2

ALPH = 'abcdefghijklmnopqrstuvwxyz'
DICT_URL = 'https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co&pathrev=61569'

def get_words(length):
    data = urllib2.urlopen(DICT_URL)
    words = [w.strip().lower() for w in data if len(w.strip()) == length]
    return words


class WordNode(object):
    def __init__(self, word, numstep):
        self.numstep = numstep
        self.word = word


def word_lader(start_word, end_word, word_set):
    queue = []
    queue.append(WordNode(start_word,1))
    word_set.add(end_word)

    while len(queue) > 0:
        top = queue.pop(0)
        word = top.word

        if word == end_word:
            return top.numstep

        arr = list(word)

        for i in range(len(arr)):
            for c in ALPH:
                temp = arr[i]
                if not arr[i] == c:
                    arr[i] = c
                new_word = ''.join(arr)
                if new_word in word_set:
                    word_set.remove(new_word)
                    queue.append(WordNode(new_word, top.numstep + 1))
                arr[i] = temp


if __name__ == "__main__":
    from_word = 'hit'
    to_word = 'cog'
    words_set = set(get_words(len(from_word)))
    short_set = set(["hot","dot","dog","lot","log"]) 
    print(word_lader(from_word, to_word, short_set))
    print(word_lader(from_word, to_word, words_set))
