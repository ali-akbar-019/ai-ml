rows = 5
row = 1
while row <= rows:
    col = 1
    while col <= row:
        print("*", end="")
        col+=1

    print()
    row+=1


row = 1
while row <= rows:
    col = 1
    while col <= rows:
        print("*", end="")
        col+=1
    print()

    row+=1

row = 1
while row <= rows:
    col = 1
    while col <= row:
        print(col, end="")
        col+=1
    print()
    row+=1


row = 1
while row <= rows:
    col = 1
    ch = ord('A')
    while col <= row:
        print(chr(ch), end="")        
        col+=1
        ch +=1
    print()
    row+=1
