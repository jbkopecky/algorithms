ALPH = 'abcdefghijklmnopqrstuvwxyz'


class WordNode(object):
    def __init__(self, word, numstep, previous_word):
        self.numstep = numstep
        self.word = word
        self.pre = previous_word

    def get_parents(self):
        result = []
        result.append(self.word)
        top = self.pre
        while top is not None:
            result.append(top.word)
            top = top.pre
        return result


def word_lader_ii(start_word, end_word, word_set):
    result = []
    queue = []
    queue.append(WordNode(start_word, 1, None))
    word_set.add(end_word)

    minstep = 0

    visited = set()
    unvisited = word_set.copy()

    prenumsteps = 0

    while len(queue) > 0:
        top = queue.pop(0)
        word = top.word
        curnumsteps = top.numstep

        if curnumsteps > len(word_set):
            return result

        if word == end_word:
            if minstep == 0:
                minstep = top.numstep
            if top.numstep == minstep and minstep != 0:
                result.append(top.get_parents())
                continue

        if prenumsteps < curnumsteps:
            unvisited.difference(visited)

        prenumsteps = curnumsteps

        arr = list(word)
        for i in range(len(arr)):
            for c in ALPH:
                temp = arr[i]
                if arr[i] != c:
                    arr[i] = c
                new_word = ''.join(arr)
                if new_word in unvisited:
                    visited.add(new_word)
                    queue.append(WordNode(new_word, top.numstep + 1, top))
                arr[i] = temp

    return result


if __name__ == "__main__":
    from_word = 'hit'
    to_word = 'cog'
    short_set = set(["hot","dot","dog","lot","log"]) 
    print(word_lader(from_word, to_word, short_set))
