def spin_words(sentence):
    s = sentence.split()
    ciag = []
    for k in s:
        if len(k) >= 5:
            p = k[::-1]
            ciag.append(p)
        else:
            ciag.append(k)
    print(ciag)
    return ciag

x = "Hey fellow warriors"
spin_words(x)

# wypisuje dobrze ale w tablicy a nie stringu :) zrob cos z tym