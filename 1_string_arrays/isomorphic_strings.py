def is_isomorphic(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return False
    if len(s1) != len(s2):
        return False
    map = {}
    for i in range(len(s1)):
        c1 = s1[i]
        c2 = s2[i]
        if c1 in map:
            if c2 != map[c1]:
                return False
        elif c2 in map.values():
            return False
        else:
            map[c1] = c2
    return True


if __name__ == "__main__":
    sa1, sa2 = 'egg', 'add'
    sb1, sb2 = 'foo', 'bar'
    print(is_isomorphic(sa1, sa2))
    print(is_isomorphic(sb1, sb2))

