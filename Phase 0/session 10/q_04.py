def func(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

func(name="ali", age=22, country="pakistan")

sq =lambda x:x**2
print(sq(2))

ad = lambda x,y: x +y
print(ad(1,2))

lr = lambda x, y: x if x > y else y

print(lr(2,3))

srt = lambda ls: sorted(ls)
print(srt([5,6,3,26,482,7,23]))