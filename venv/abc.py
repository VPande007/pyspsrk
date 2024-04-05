x = ["a","b","c","a","b","c","d","e","a","e"]


def list(a):
    z = []

    for i in x:
        if i in z:
            pass
        else:
            z.append(i)
    return z

print(list(x))

