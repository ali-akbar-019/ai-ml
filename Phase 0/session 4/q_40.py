num = 12345

ans = 0
while num != 0:
    dig = num % 10
    ans = ans * 10 + dig
    num = num // 10
print(f"ans: {ans}")