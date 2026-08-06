# a simple to do

def addTodo():
    with open("todos.txt", "a") as f:
        todo = input("Todo: ")
        _id= int(input("Please enter a unique id for it: "))

        f.write(f"{_id} - {todo} \n")
    f.close()
    menu()
def readAllTodo():
    print("-"*50)
    print("---All Todos---")
    with open("todos.txt", "r") as f:
        for todo in f:
            print(todo.strip())        
    f.close()
    print("-"*50)
    menu()
  

def markTodoDone():
    output = ""

    with open("todos.txt", "r") as f:
        _id = int(input("Enter id: "))
        for todo in f:
            if todo.startswith(f"{_id}"):
                output += f"{todo.strip()} - Done\n"
            else:
                output+= todo


    with open('todos.txt', 'w') as f:
          f.write(output) 

    f.close()
    menu()
        
def menu():
    choice = int(input("""
1. Add Todo
2. Read All Todos
3. Mark todo Done
4. Exit
"""))

    if choice == 1:
        addTodo()
    elif choice == 2:
        readAllTodo()
    elif choice == 3:
        markTodoDone()
    else:
        return

if __name__ == "__main__":
    menu()
