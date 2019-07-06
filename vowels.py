n=input()
v="a","e","i","o","u"
if n in v:
    print("vowels")
elif n.isalpha():
    print("Consonant")
else:
    print("invalid")
