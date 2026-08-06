def func(name, age):
    print(f"{name} is {age} years old")

func("ali akbar", 22)

def func1(*args):
    return sum(args)

print("sum: ",func1(1,2,3,43,4,45,6,7,2))
def func2(*args):
    sum1 = sum(args)
    cnt = len(args)
    return sum1 / cnt
print(f"average: {func2(1,2,3,43,4,45,6,7,2):.2f}")