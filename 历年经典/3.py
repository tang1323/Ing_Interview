w = input()
for x in w:
    if '0' <= x <= '9':
        continue
    else:
        w.replace(x, '')
print(w)














