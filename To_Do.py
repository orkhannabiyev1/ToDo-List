from operator import index

list=[]
def show():
    if not list:
        print("\nYou have no task yet!")
    else:
        print("\nTODO List:")
        for idx, task in enumerate(list, start=1):  # Using enumerate for correct indexing
            print(f"{idx}. {task}")
def add():
    b=input("\nWrite the task you want to add: ")
    list.append(b)
def remove():
    c=int(input("\nWrite number of task: "))
    removed_task=list.pop(c-1



def main():
    while True:
        print("\n--- TODO LIST ---")
        print("1. Show TODO List")
        print("2. Add TODO")
        print("3. Remove TODO")
        print("4. Exit")
        a = int(input("\nChoose one (1-4): "))
        if a==1:
            show()
        if a==2:
            add()
        if a==3:
            remove()
        if a==4:
            break
main()






