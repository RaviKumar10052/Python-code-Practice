s= input()
l=s.split(" ")
word="\n"
for x in l:
    if len(x)>len(word):
        word=x
print(word)


