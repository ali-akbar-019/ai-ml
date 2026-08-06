# with open("users.txt", "a") as f:
#     for i in range(10):
#         name = input("Enter a name: ")
#         f.write(f"User {i + 1}: {name}\n")
        

with open("users.txt", "r") as f:
    for user in f:
        if "ali" in user:
            print("specia user: ", user)
        else: print(user.strip())