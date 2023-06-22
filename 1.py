'''def strcounter(s):
    for syn in set(s):
        count = 0
        for supsym in s:
            if syn == supsym:
                count+=1
        print(syn, count)

str="abca"
strcounter(str)


def strcounter(s):
    sym_count={}
    for sym in s:
        sym_count[sym] = sym_count.get(sym, 0) +1
    for sym, count in sym_count.items():
        print(sym, count)
print('АЗАЗАЗАЗАЗАЗА')'''
def palindrome(s):
    if s[::-1]==s:
        print('True')
    else:
        print('False')

while True:
    s = input("введите слово: ")
    palindrome(s)