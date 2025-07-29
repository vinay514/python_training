char_count={}
name="hi how are you"
for c in name:
    if c not in char_count:
        char_count[c]=1
    else:
        char_count[c]+=1
        print(char_count)