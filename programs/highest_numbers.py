items=[10,20,100,2,8,1]
highest=items[0] # assume
for i in items:
    if i>highest:
        highest=i
print(f"{highest} is highest number from the items")

second_highest=items[0]
for i in items:
    if i!=highest and i>second_highest:
        second_highest=i
print(f"{second_highest} is second_highest number from the items")

lowest=items[0]
for i in items:
    if i<lowest:
        lowest=i
print(f"{lowest} is lowest number from the items")

second_lowest=None
for i in items:
    if i!=lowest:
        if second_lowest is None or i<second_lowest:
           second_lowest=i
print(f"{second_lowest} is second_lowest number from the items")
