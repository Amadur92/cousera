def reverse_words(s):
    s = s.split()
    return s[1] + " " + s[0]


print(reverse_words(input()))
