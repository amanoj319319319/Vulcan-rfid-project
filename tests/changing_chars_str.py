city="southafrica"
target_char="f"
result=""
repeated_num=1
count=0
for i, ch in enumerate(city):
    if ch == target_char:
        count=count+1
        if count==1:
            result=result+ch.upper()
        else:
            result=result+ch
    else:
        result=result+ch
city=result
print(f"after changing small case f into upper case f, city becomes as:-", city)
