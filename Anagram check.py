s1 = 'listen'
s2 = 'sent'
# sa=sorted(s1)
# sb=sorted(s2)
def anagram(s1,s2):
    if len(s1) == len(s2):
        sa=sorted(s1)
        sb=sorted(s2)
        if sa == sb:
            print("s1 and s2 is anagram")
    else:
        print("not an anagram")
anagram(s1,s2)
