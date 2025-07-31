vowels_1=[]
cons_1=[]
name="southafrica"
def vowels_cons(name):
    for i in name:
        if i in "aeiou":
            vowels_1.append(i)
        else:
            cons_1.append(i)
print(f"vowels are:", vowels_1)
print(f"cons_are:", cons_1)
print("i am second line")
print("i am third line")
print("i am fourth line")
