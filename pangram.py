string=input("enter sentence")
stringd=set(string)
list = []
for i in range(97,123):
    list.append(chr(i))
if stringd in list:
    print("pangram")
else:
    print("not pangram")
