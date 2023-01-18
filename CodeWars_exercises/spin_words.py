def spin_words(sentence):
    s = sentence.split()
    ciag = []
    for k in s:
        if len(k) >= 5:
            p = k[::-1]
            ciag.append(p)
        else:
            ciag.append(k)
    return ciag

x = "Hey fellow warriors"


def listToString(s):

    str1 = " "

    return print(str1.join(s))


listToString(spin_words(x))