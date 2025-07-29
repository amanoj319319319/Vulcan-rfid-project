def is_prime(num):
    if num==0 or num==1:
        return False
    for i in range(2,num):
        if num%2 == 0:
            return False
    return True
num=11
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
print("program is finished")
print("hello prime")
a=10