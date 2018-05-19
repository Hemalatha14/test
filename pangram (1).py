string=input("enter sentence")
stringd=set(string.lower())
l = []
for i in stringd:
    if ord(i) in range(97,123):
        l.append(i)
if len(l)==26:
    print("pangram")
else:
    print("not pangram")
