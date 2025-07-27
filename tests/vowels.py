name="southafrica"
vowels=[]
cons=[]
for i in name:
    if i in "aeiou":
        vowels.append(i)
    else:
        cons.append(i)
print(f"{vowels} are vowels")
print(f"{cons} are cons")
print("program is ended")
