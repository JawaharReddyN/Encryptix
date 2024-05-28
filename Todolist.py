class ToDoList:
    def __init__(self): 
        self.tasks =[]

    def addtask(self,task):
        self.tasks.append(task)  
        print("Task is added successfully")

    def viewtasks(self):
        if not self.tasks:  
           print("No Task is added till now")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}.{task}")

    def updatetask(self,index,newtask):
        if 1 <= index <= len(self.tasks):
            self.tasks[index -1]= newtask
            print("Task is updated now")
        else:
            print("Task index is Invalid") 

    def deltask(self,index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index -1]
            print("Task is deleted sucessfully")
        else:
            print("Task index is Invalid")
            
def main():
    todo_list = ToDoList()
    
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Update Tasks")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice:")

        if choice == '1':
            task = input("Enter task:")
            todo_list.addtask(task)
        elif choice == '2':
            todo_list.viewtasks()
        elif choice == '3':
            index = int(input("Enter task index to update:"))
            new_task = input("Enter new task:")
            todo_list.updatetask(index,new_task)
        elif choice == '4':
            index = int(input("Enter task index to delete particular task:"))
            todo_list.deltask(index) 
        elif choice == '5':
            print("Exit")
            break
        else:
            print("Invalid choice! Try again")

if __name__ == "__main__":
    main()

                                  