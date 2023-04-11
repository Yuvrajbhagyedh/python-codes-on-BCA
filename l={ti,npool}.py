l={"t":"i","n":"pool"}
print(l)
if "p" in l:
    print("yes")
else:
    print("no")
print(l["n"])
print(l.get("t"))
l["n"]="op"
print(l)
print(len(l))